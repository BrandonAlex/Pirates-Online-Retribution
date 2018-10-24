(function (container) {
    var _w = {
        /**
         * Constants
         */
        version: "1.16.4",

        TPA_INTENT:"TPA",
        firstAddEventListenerCall:true,

        MessageTypes:{
            CHANGE_APP_SIZE:"changeWindowSize",
            RESIZE_WINDOW:"resizeWindow",
            REFRESH_APP:"refreshApp",
            APP_IS_ALIVE:"appIsAlive",
            APP_STATE_CHANGED:"appStateChanged",
            CLOSE_POPUP:"closePopup",
            OPEN_POPUP:"openPopup",
            OPEN_MODAL:"openModal",
            OPEN_MEDIA_DIALOG:"openMediaDialog",
            OPEN_FULLSCREEN:"openFullscreen",
            OPEN_BILLING_PAGE:"openBillingPage",
            SM_REQUEST_LOGIN:"pingpong:smRequestLogin",
            SM_CURRENT_MEMBER:"pingpong:smCurrentMember",
            SITE_INFO:"pingpong:siteInfo",
            EVENT_LISTENER_ADDED:"pingpong:addEventListener",
            // Deprecated
            HEIGHT_CHANGED:"heightChanged",
            APP_SETTINGS_CHANGED:"appSettingsChanged",
            APP_SETTINGS_CLOSE:"appSettingsClose",
            APP_SHOW_POPUP:"appShowPopup",
            NAVIGATE_TO_STATE: "navigateToState"
        },

        Origin: {
            /* TOP LEFT corner is the default */
            DEFAULT: 'TOP_LEFT',

            /* corners enumeration */
            TOP_LEFT: 'TOP_LEFT',
            TOP_RIGHT: 'TOP_RIGHT',
            BOTTOM_RIGHT: 'BOTTOM_RIGHT',
            BOTTOM_LEFT: 'BOTTOM_LEFT'
        },

        EventsCallbacks:{},

        compId: null,

        callbacks: {},
        callId: 1,

        /**
         * Functions
         */
        sendMessageInternal:function (type, data) {
            var target = parent.postMessage ? parent : (parent.document.postMessage ? parent.document : undefined);
            if (target && typeof target != "undefined") {
                target.postMessage(JSON.stringify({
                    intent:_w.TPA_INTENT,
                    compId:_w.compId,
                    type:type,
                    data:data
                }), "*");

                var dataStr = "";
                try {
                    dataStr = JSON.stringify(data);
                } catch(err) {}
                _w.trackSDKCall(type, dataStr);
            }
        },

        sendMessageInternal2:function (msgType, params, callback) {
            if (!msgType) { // || _w.MessageTypes[msgType]) {
                return;
            }

            /* prepare call parameters */
            var blob = _w.getBlob(msgType, params, callback);
            

            var target = parent.postMessage ? parent : (parent.document.postMessage ? parent.document : undefined);
            if (target && typeof target != "undefined") {
                var dataStr = "";
                try {
                    dataStr = JSON.stringify(params);
                } catch(err) {
                    // ...
                }

                target.postMessage(JSON.stringify(blob),"*");

                _w.trackSDKCall(msgType, dataStr);
            }
        },

        getBlob: function(msgType, params, onResponseCallback) {
            var blob = {
                intent: "TPA2",
                callId: this.getCallId(),
                type: msgType,
                compId: _w.compId,
                params: params
            };

            if (onResponseCallback) {
                this.callbacks[blob.callId] = onResponseCallback;
            };

            return blob;
        },

        getCallId: function() {
           return _w.callId++;
        },

        /** Function sendPingPongMessage
         *  sends a post message to TPAManager (viewer) with message type and invokes the callback
         * @param type - a property of MessageTypes
         * @param callback
         * @param runMultipleTimes - optional, if set to true the post message callback isn't removed
         */
        sendPingPongMessage:function (type, callback, runMultipleTimes) {
            this.sendMessageInternal(type);

            var onMessageCallback = function (evt) {
                var postMessageData = JSON.parse(evt.data);
                if (postMessageData.intent == _w.TPA_INTENT) {
                    if (postMessageData.type == type && callback) {
                        callback(postMessageData.data);
                        if (!runMultipleTimes) {
                            this._removePostMessageCallback(onMessageCallback);
                        }
                    }
                }
            }.bind(this);

            this.addPostMessageCallback(onMessageCallback);
        },

        addPostMessageCallback:function (callback) {
            if (window.addEventListener) {
                window.addEventListener('message', callback, false);
            } else if (window.attachEvent) {
                window.attachEvent('onmessage', callback);
            }
        },

        _removePostMessageCallback:function (callback) {
            if (window.removeEventListener) {
                window.removeEventListener('message', callback);
            } else if (window.detachEvent) {
                window.detachEvent('onmessage', callback);
            }
        },

        getQueryParameter:function (parameterName) {
            var queryString = location.search.substring(1);
            parameterName += "=";
            if (queryString.length > 0) {
                var begin = queryString.indexOf(parameterName);
                if (begin != -1) {
                    begin += parameterName.length;
                    var end = queryString.indexOf("&", begin);
                    if (end == -1) {
                        end = queryString.length;
                    }
                    return unescape(queryString.substring(begin, end));
                }
            }
            return null;
        },

        decodeBase64: function(str) {
            var e={},i,k,v=[],r='',w=String.fromCharCode;
            var n=[[65,91],[97,123],[48,58],[43,44],[47,48]];

            for(z in n){for(i=n[z][0];i<n[z][1];i++){v.push(w(i));}}
            for(i=0;i<64;i++){e[v[i]]=i;}

            for(i=0;i<str.length;i+=72){
            var b=0,c,x,l=0,o=str.substring(i,i+72);
                 for(x=0;x<o.length;x++){
                        c=e[o.charAt(x)];b=(b<<6)+c;l+=6;
                        while(l>=8){r+=w((b>>>(l-=8))%256);}
                 }
            }
            return r;
        },

        getVersion: function() {
            var version = !!_w.version ? _w.version : (window.location.pathname.split('/')[3] || "unknown");

            return version;
        },

        gaInit: function() {
            var _gaq = window._gaq || ( window._gaq = []);
            _gaq.push(['wix._setAccount', 'UA-2117194-51']);
            _gaq.push(['wix._trackPageview']);

            (function() {
              var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
              var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        },

        errorTrackingInit: function() {
            var event = 'onerror';
            var listener =  _w.errorHandler;

            if (window.addEventListener) {
                window.addEventListener(event.replace(/^on/, ''), listener, false);
            } else {
                if (window[event]) {
                    var origListener = window[event];
                    window[event] = function(event) {
                        origListener(event);
                        listener(event);
                    }
                } else {
                    window[event] = function(event) {
                        listener(event);
                    }
                }
            }
        },

        errorHandler: function(errorMsg, url, lineNumber) {
            _w.trackError(errorMsg, lineNumber);

            return false;
        },

        /** Function trackEvent
         *
         * Add an event tracking
         *
         * @param category (String) name for the group of objects you want to track.
         * @param action (String) action name, unique in the category scope used to define the type of user interaction.
         * @param label (String) Optional, provides additional dimensions to the event data
         * @param value (Number) Optional, provides numerical data about the user event
         */
        gaTrackEvent: function(category, action, label, value) {
            _gaq.push(['wix._trackEvent', category || "default", action || "default", label || "", value]);
        },

        trackSDKCall: function(callName, label) {
            _w.gaTrackEvent("SDK", callName, label);
        },

        trackEventCall: function(eventName) {
            _w.gaTrackEvent("Event", eventName);
        },

        trackError: function(errorMessage) {
            _w.gaTrackEvent("Error", errorMessage);
        },

        initEventsCallbacks: function(events) {
            for (var propertyName in events) {
                if (events.hasOwnProperty(propertyName)) {
                    _w.EventsCallbacks[propertyName] = [];
                }
            }
        },

        getDecodedInstance: function() {
            var instanceStr = _w.getQueryParameter("instance");
            var encodedInstance = instanceStr.substring(instanceStr.indexOf(".")+1);
            return JSON.parse(this.decodeBase64(encodedInstance));
        },

        getInstanceValue: function(key) {
            var decodedInstance = _w.getDecodedInstance();
            if (decodedInstance) {
                return decodedInstance[key];
            }
            return null;
        },

        receiver:function (event) {
            if (!event || !event.data) {
                return;
            }

            var data = {};

            try {
                data = JSON.parse(event.data);
            } catch(e) {
                return;
            };

            switch(data.intent) {
                case "TPA_RESPONSE":
                    if (data.callId && this.callbacks[data.callId]) {
                        this.callbacks[data.callId](data.status, data.res);
                        delete this.callbacks[data.callId];
                    }
                    break;

            case "addEventListener":
                _w.trackEventCall(data.eventType);
                this.EventsCallbacks[data.eventType].forEach(
                    function (callback) {
                        callback.apply(this, [data.params]);
                    });
                break;
            }
        }
    };

    /**
     * Public API definition
     */
    var API = {
        /**
         * @private current edit mode state
         */
        _currentEditMode: 'editor',

        /**
         * @private DO NOT USE!!! - initialization function
         */
        _init:function () {
            _w.gaInit();
            _w.initEventsCallbacks(this.Events);
            _w.errorTrackingInit();

            _w.compId = _w.getQueryParameter("compId") || "[UNKNOWN]";

            this.currentEditMode = _w.getQueryParameter("viewMode");
            this.addEventListener(this.Events.EDIT_MODE_CHANGE, function(params) {
                this.currentEditMode = params.editMode;
            }.bind(this));
            // report ready to Wix
            _w.sendMessageInternal(_w.MessageTypes.APP_IS_ALIVE, {version: _w.getVersion()});
        },

        /**
         * Supported events - some are relevant for the editor only
         */
        Events:{
            /**
             * @since SDK 1.11.0
             * Signal transition between editor and preview modes
             */
            EDIT_MODE_CHANGE:'EDIT_MODE_CHANGE',
            /**
             * @since SDK 1.11.0
             * Signal page navigation, relevant for editor, preview & site
             */
            PAGE_NAVIGATION_CHANGE:'PAGE_NAVIGATION_CHANGE',
            /**
             * @since SDK 1.13.0
             * Signal Site publishing - editor only
             */
            SITE_PUBLISHED: 'SITE_PUBLISHED',
            /**
             * @since SDK 1.13.0
             * Signal Component deletion in the editor
             */
            COMPONENT_DELETED: 'COMPONENT_DELETED',
            /**
             * @private
             */
            ON_MESSAGE_RESPONSE: "ON_MESSAGE_RESPONSE"
        },

        Origin: _w.Origin,

        Settings: {
            /** Function getSiteInfo
             *
             * Returns the site information in a callback function
             *
             * @since SDK 1.12.0
             * @param onSuccess (Function) callback function: function(params) {...}
             */
            getSiteInfo: function(onSuccess) {
                Wix.getSiteInfo(onSuccess);
            },

            /** Function refreshApp
             *
             * Refresh all app's components
             *
             * @since SDK 1.12.0
             * @param queryParams
             */
            refreshApp: function(queryParams) {
                this.refreshAppByCompIds(null, queryParams);
            },

            /** Function refreshAppByCompIds
             *
             * Refresh a specific app's components
             *
             * @since SDK 1.12.0
             * @param compIds (String) a component id
             * @param queryParams (String) custom query parameters to pass to the component
             */
            refreshAppByCompIds: function(compIds, queryParams) {
                _w.sendMessageInternal(_w.MessageTypes.APP_SETTINGS_CHANGED, {'queryParams':queryParams, 'compIds':compIds});
            },

            /** Function openBillingPage
             *
             * @since SDK 1.13.0
             * Opens the Wix billing page in a new tab/window
             */
            openBillingPage: function() {
                _w.sendMessageInternal(_w.MessageTypes.OPEN_BILLING_PAGE);
            }
        },

        Utils: {
            /**
               * Function getCompId
               *
               * @since SDK 1.12.0
               * @return (String) the widget/section/settings iframe's component id
            */
            getCompId: function(){
                _w.trackSDKCall("Utils.getCompId");
                return _w.compId;
            },

            /**
             * Function getOrigCompId
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns origCompId parameter value, otherwise returns null
             */
            getOrigCompId: function(){
                _w.trackSDKCall("Utils.getOrigCompId");
                return _w.getQueryParameter("origCompId");
            },

            /**
             * Function getViewMode
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns viewMode parameter value, otherwise returns null
             */
            getViewMode: function(){
                _w.trackSDKCall("Utils.getViewMode");
                return Wix.currentEditMode;
            },

            /**
             * Function getWidth
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns width parameter value, otherwise returns null
             */
            getWidth: function(){
                _w.trackSDKCall("Utils.getWidth");
                return _w.getQueryParameter("width");
            },

            /**
             * Function getLocale
             *
             * @since SDK 1.14.0
             * @return for valid endpoints returns locale parameter value, otherwise returns null
             */
            getLocale: function(){
                _w.trackSDKCall("Utils.getLocale");
                return _w.getQueryParameter("locale");
            },

            /**
             * Function getCacheKiller
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns cacheKiller parameter value, otherwise returns null
             */
            getCacheKiller: function(){
                _w.trackSDKCall("Utils.getCacheKiller");
                return _w.getQueryParameter("cacheKiller");
            },

            /**
             * Function getTarget
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns target parameter value, otherwise returns null
             */
            getTarget: function(){
                _w.trackSDKCall("Utils.getTarget");
                return _w.getQueryParameter("target");
            },

            /**
             * Function getSectionUrl
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns section-url parameter value, otherwise returns null
             */
            getSectionUrl: function(){
                _w.trackSDKCall("Utils.getSectionUrl");
                return _w.getQueryParameter("section-url").slice(0, -1);
            },

            /**
             * Function getInstanceId
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns instanceId app instance property value, otherwise returns null
             */
            getInstanceId: function(){
                _w.trackSDKCall("Utils.getInstanceId");
                return _w.getInstanceValue("instanceId");
            },

            /** Function getSignDate
             *
             * @deprecated  As of SDK 1.13.0
             * @return for valid endpoints returns signDate app instance property value, otherwise returns null
             */
            getSignDate: function(){
                _w.trackSDKCall("Utils.getSignDate");
                return _w.getInstanceValue("signDate");
            },

            /**
             * Function getUid
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns uid app instance property value, otherwise returns null
             */
            getUid: function(){
                _w.trackSDKCall("Utils.getUid");
                return _w.getInstanceValue("uid");
            },

            /**
             * Function getPermissions
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns permissions app instance property value, otherwise returns null
             */
            getPermissions: function(){
                _w.trackSDKCall("Utils.getPermissions");
                return _w.getInstanceValue("permissions");
            },

            /**
             * Function getIpAndPort
             *
             * @deprecated  As of SDK 1.13.0
             * @return for valid endpoints returns ipAndPort app instance property value, otherwise returns null
             */
            getIpAndPort: function(){
                _w.trackSDKCall("Utils.getIpAndPort");
                return _w.getInstanceValue("ipAndPort");
            },

            /**
             * Function getDemoMode
             *
             * @since SDK 1.12.0
             * @return for valid endpoints returns demoMode app instance property value, otherwise returns null
             */
            getDemoMode: function(){
                _w.trackSDKCall("Utils.getDemoMode");
                return _w.getInstanceValue("demoMode");
            }
        },

        /**
         * Function reportHeightChange
         *
         * @since SDK 1.8.0
         * @param height (Number) new component height
         */
        reportHeightChange:function (height) {
            _w.sendMessageInternal(_w.MessageTypes.HEIGHT_CHANGED, height);
        },

        /**
         * Function pushState
         *
         * @since SDK 1.8.0
         * @param state (String) new app's state to push into the editor history stack
         */
        pushState:function (state) {
            _w.sendMessageInternal(_w.MessageTypes.APP_STATE_CHANGED, state);
        },

        /**
         * Function refreshApp
         *
         * @deprecated SDK 1.12.0
         * @param queryParams (Array) component ids for which a refresh is required
         */
        refreshApp:function (queryParams) {
            this.refreshAppByCompIds(null, queryParams);
        },

        /**
         * Function refreshAppByCompIds
         *
         * @deprecated SDK 1.12.0
         * @param compIds (Array) component ids for which a refresh is required
         * @param queryParams ()
         */
        refreshAppByCompIds:function (compIds, queryParams) {
            _w.sendMessageInternal(_w.MessageTypes.APP_SETTINGS_CHANGED, {'queryParams':queryParams, 'compIds':compIds});
        },

        /**
         * Function requestLogin
         *
         * @since SDK 1.3.0
         * @param onSuccess (Function) a callback function to receive the operation completion
         * status. The function signature should be :
         *  function onSuccess(param) {...}
         */
        requestLogin:function (onSuccess) {
            _w.sendPingPongMessage(_w.MessageTypes.SM_REQUEST_LOGIN, onSuccess);
        },

        /**
         * Function getSiteInfo
         *
         * @param onSuccess (Function) a callback function to receive the function completion
         * status. The function signature should be :
         *  function onSuccess(param) {...}
         */
        getSiteInfo:function (onSuccess) {
            _w.sendPingPongMessage(_w.MessageTypes.SITE_INFO, onSuccess);
        },

        /**
         * Function currentMember
         *
         * @since SDK 1.6.0
         * @param onSuccess (Function) a call back function to receive the function completion
         * status. The function signature should be :
         *  function onSuccess(param) {...}
         */
        currentMember:function (onSuccess) {
            _w.sendPingPongMessage(_w.MessageTypes.SM_CURRENT_MEMBER, onSuccess);
        },

        /**
         * Function openPopup
         *
         * @experimental
         * @param url (String) popup iframe's url
         * @param x (Number) popup horizontal offset from origin point
         * @param y (Number) popup vertical offset from origin point
         * @param width (Number) popup width in pixels
         * @param height (Number) popup height in pixels
         * @param origin (String, optional) popup origin point, reserved values, one of Origin's values
         *        example - TOP_LEFT, TOP_RIGHT, etc.
         */
        openPopup:function (url, width, height, position) {
            position = position || { x:0, y:0, origin:this.Origin.DEFAULT };

            var args = {
                url   : url,
                origin: position.origin,
                x     : position.x,
                y     : position.y,
                width : width,
                height: height
            };
            _w.sendMessageInternal(_w.MessageTypes.OPEN_POPUP, args);
        },

        /*
         * Function closeWindow
         *
         * Closes the app's modal/popup window.
         * This function can be used from a popup scope only!!
         *
         * @since SDK 1.13.0
         */
        closeWindow:function () {
            _w.sendMessageInternal(_w.MessageTypes.APP_SETTINGS_CLOSE);
        },

        /**
         * Function openModal
         *
         * @since SDK 1.13.0
         * @param url (String) popup iframe's url
         * @param width (Number) popup width in pixels
         * @param height (Number) popup height in pixels
         */
        openModal:function (url, width, height) {
            if (this.Utils.getViewMode() != "editor") {
                var args = {
                    url   : url,
                    width : width,
                    height: height
                };
                _w.sendMessageInternal(_w.MessageTypes.OPEN_MODAL, args);
            }
        },

        /**
         * Function resizeWindow
         *
         * @experimental
         * @param width (Number) in pixels
         * @param height (Number) in pixels
         */
        resizeWindow:function (width, height) {
            _w.sendMessageInternal(_w.MessageTypes.RESIZE_WINDOW, {width:width, height:height});
        },

        /**
         * Function addEventListener
         *
         * @since SDK 1.11.0
         * @param eventName (String) the event name, reserved values, see Events
         * @param callBack (Function) a callback function which gets invoked when a new
         * event is sent from the wix site, The function signature should be :
         *  function callBack(param) {...}
         */
        addEventListener: function(eventName, callBack) {
            var callbacks = _w.EventsCallbacks[eventName] || [];
            callbacks.push(callBack);
            if (_w.firstAddEventListenerCall) {
                _w.addPostMessageCallback(_w.receiver.bind(_w));
                _w.firstAddEventListenerCall = false;
            }
        }

    };

    /**
     * Compatabilty script to support bind on iOS5
     */
    if (!Function.prototype.bind) {
        Function.prototype.bind = function (oThis) {
            if (typeof this !== "function") {
                // closest thing possible to the ECMAScript 5 internal IsCallable function
                throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");
            }
            var aArgs = Array.prototype.slice.call(arguments, 1),
                fToBind = this,
                fNOP = function () {},
                fBound = function () {
                    return fToBind.apply(this instanceof fNOP && oThis
                        ? this
                        : oThis,
                        aArgs.concat(Array.prototype.slice.call(arguments)));
                };
            fNOP.prototype = this.prototype;
            fBound.prototype = new fNOP();

            return fBound;
        };
    }

    /**
     * Deploy API on the container (iframe window)
     */
    API._init();
    container.Wix = API;
}(this));
