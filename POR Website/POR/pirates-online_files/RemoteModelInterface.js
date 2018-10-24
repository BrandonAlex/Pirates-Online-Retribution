(function webpackUniversalModuleDefinition(root, factory) {
  if(typeof exports === 'object' && typeof module === 'object')
    module.exports = factory();
  else if(typeof define === 'function' && define.amd)
    define([], factory);
  else if(typeof exports === 'object')
    exports["RemoteModelInterface"] = factory();
  else
    root["RemoteModelInterface"] = factory();
})(this, function() {

  var DATA = 'data',
    STATE = 'state',
    TYPE = 'type',
    PROPS = 'props',
    PARENT = 'parent',
    EVENTS = 'events',
    LAYOUT = 'layout',
    BEHAVIOR = 'behavior',
    PUBLIC_API = 'publicAPI',
    IS_DISPLAYED = 'isDisplayed';

  function RemoteModelInterface(modelJson, onUpdateCallback) {
    this._model = modelJson || {components: {}, connections: {}, pages: {}};
    this._onUpdateCallback = onUpdateCallback;
    this._eventHandlers = {};
  }

  RemoteModelInterface.prototype.addComponent = function(compId, compDescriptor) {
    var comp = {};
    comp[PARENT] = compDescriptor[PARENT];
    comp[STATE] = compDescriptor[STATE] || {};
    comp[TYPE] = compDescriptor[TYPE];
    comp[DATA] = compDescriptor[DATA] || {};
    comp[PROPS] = compDescriptor[PROPS] || {};
    comp[LAYOUT] = compDescriptor[LAYOUT] || {};
    comp[EVENTS] = compDescriptor[EVENTS] || [];
    comp[IS_DISPLAYED] = compDescriptor[IS_DISPLAYED] || false;
    this._model.components[compId] = comp;
  };

  RemoteModelInterface.prototype.addPagesData = function(pagesData) {
    this._model.pages.pagesData = pagesData.pagesData;
    this._model.pages.currentPageId = pagesData.currentPageId;
    this._model.pages.baseUrl = pagesData.baseUrl;
  };

  RemoteModelInterface.prototype.addConnections = function(connectionsModel) {
    this._model.connections = connectionsModel;
  };

  //Getters

  RemoteModelInterface.prototype.getComp = function (compId) {
    return _.get(this._model.components, compId);
  };

  RemoteModelInterface.prototype.getState = function(compId) {
    return _.get(this._model.components, [compId, STATE]);
  };

  RemoteModelInterface.prototype.getData = function(compId) {
    return _.get(this._model.components, [compId, DATA]);
  };

  RemoteModelInterface.prototype.getType = function(compId) {
    return _.get(this._model.components, [compId, TYPE]);
  };

  RemoteModelInterface.prototype.getProps = function(compId) {
    return _.get(this._model.components, [compId, PROPS]);
  };

  RemoteModelInterface.prototype.getEvents = function(compId) {
    return _.get(this._model.components, [compId, EVENTS]);
  };

  RemoteModelInterface.prototype.getLayout = function(compId) {
    return _.get(this._model.components, [compId, LAYOUT]);
  };

  RemoteModelInterface.prototype.getPublicAPI = function(compId) {
    return _.get(this._model.components, [compId, PUBLIC_API]);
  };

  RemoteModelInterface.prototype.getCallbackById = function(callbackId) {
    return this._eventHandlers[callbackId];
  };

  RemoteModelInterface.prototype.getParent = function(compId) {
    return _.get(this._model.components, [compId, PARENT]);
  };

  RemoteModelInterface.prototype.getChildren = function(parentId) {
    var compIds = getCompIds(this._model);
    return compIds.filter(function (compId) {
      return (_.get(this._model.components, [compId, PARENT]) === parentId);
    }, this);
  };

  //Setters

  RemoteModelInterface.prototype.setData = function(compId, partialData) {
    set(this._model, compId, DATA, partialData, this._onUpdateCallback);
  };

  RemoteModelInterface.prototype.setProps = function(compId, partialProps, cb) {
    set(this._model, compId, PROPS, partialProps, function (compId, property, partial) {
      this._onUpdateCallback.call(this, compId, property, partial, cb);
    }.bind(this));
  };

  RemoteModelInterface.prototype.setLayout = function(compId, partialLayout) {
    set(this._model, compId, LAYOUT, partialLayout, this._onUpdateCallback);
  };

  RemoteModelInterface.prototype.setPublicAPI = function(compId, api) {
    var comp = _.get(this._model.components, compId);
    if (comp) {
      comp[PUBLIC_API] = api;
    }
  };

  function executeBehavior(behaviorType, behaviorName, params, compId, callback) { // todo: why is it called execute behavior? it does not execute
    var behavior = {
      type: behaviorType,
      name: behaviorName,
      targetId: compId,
      params: params
    };

    if (this._onUpdateCallback) {
      this._onUpdateCallback(compId, BEHAVIOR, behavior, callback);
    }
  }

  RemoteModelInterface.prototype.executeCompBehavior = function (compId, behaviorName, params, callback) {
    executeBehavior.call(this, 'comp', behaviorName, params, compId, callback);
  };

  RemoteModelInterface.prototype.executeAnimation = function (compId, animationName, params, callback) {
    executeBehavior.call(this, 'animation', animationName, params, compId, callback);
  };

  RemoteModelInterface.prototype.setUpdateCallback = function(onUpdateCallback) {
    this._onUpdateCallback = onUpdateCallback;
  };

  RemoteModelInterface.prototype.registerEvent = function(widgetInstanceId, compId, eventType, callback) {
    var callbackId;

    if (_.isFunction(callback)) {
      callbackId = guid();
      var partialEvents = {};
      this._eventHandlers[callbackId] = callback;
      partialEvents[eventType] = callbackId;
    } else {
      callbackId = callback;
    }

    var actionBehavior = {
      action: {
        type: 'comp',
        name: eventType,
        sourceId: compId
      },
      behavior: {
        type: 'widget',
        targetId: widgetInstanceId,
        params: {
          callbackId: callbackId,
          compId: compId
        },
        name: 'runCode'

      }
    };
    set(this._model, compId, EVENTS, actionBehavior, this._onUpdateCallback);
  };

  RemoteModelInterface.prototype.toJson = function() {
    return this._model;
  };

  //General

  RemoteModelInterface.prototype.getScopedRMI = function(controllerId) {
    var scopedRMI = new this.constructor(this._model, this._onUpdateCallback);
    scopedRMI.getCompIdsFromRole = scopedRMI.getCompIdsFromRole.bind(scopedRMI, controllerId);
    scopedRMI.getCompIdsFromType = scopedRMI.getCompIdsFromType.bind(scopedRMI, controllerId);
    scopedRMI.getConfig = scopedRMI.getConfig.bind(scopedRMI, controllerId);
    return scopedRMI;
  };

  RemoteModelInterface.prototype.getCompIdsFromType = function(controllerId, type) {
    var compIds = getCompIds(this._model);
    var comps = [];
    compIds.forEach(function(compId) {
      var compType = this.getType(compId);
      if (compType === type) {
        comps.push(compId);
      }
    }, this);
    return comps;
  };

  RemoteModelInterface.prototype.getCompIdsFromRole = function(controllerId, role) {
    var connectionConfigs = _.get(this._model.connections, [controllerId, role]);
    return connectionConfigs ? Object.keys(connectionConfigs) : [];
  };

  RemoteModelInterface.prototype.getConfig = function(controllerId, compId, role) {
    var connectionConfigs = _.get(this._model.connections, [controllerId, role]);
    return connectionConfigs ? connectionConfigs[compId] : {};
  };

  RemoteModelInterface.prototype.getCompsFromType = function (type) {
    var comps = [];
    var compIds = getCompIds(this._model);
    compIds.forEach(function(compId) {
      var compType = this.getType(compId);
      if (compType === type) {
        comps.push(this.getComp(compId));
      }
    }, this);
    return comps;
  };

  RemoteModelInterface.prototype.updateModel = function (modelUpdates) {
    for (var compId in modelUpdates) {
      var comp = this.getComp(compId);
      var compUpdates = modelUpdates[compId];
      if (comp) {
        for (var keyToUpdate in compUpdates) {
          _.assign(comp[keyToUpdate], compUpdates[keyToUpdate]);
        }
      }
    }
  };


  //Utility

  function guid() {
    function s4() {
      return Math.floor((1 + Math.random()) * 0x10000)
        .toString(16)
        .substring(1);
    }
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
      s4() + '-' + s4() + s4() + s4();
  }

  function set(model, compId, property, partial, onUpdateCallback) {
    var comp = _.get(model, ['components', compId]);
    if (!comp) {
      return;
    }
    comp[property] = _.assign(comp[property], partial);
    if (onUpdateCallback) {
        onUpdateCallback(compId, property, partial);
    }
  }

  function getCompIds(model) {
    return Object.keys(model.components);
  }

  //////////////////////////////////// copied from lodash /////////////////////////////
//  Copyright 2012-2015 The Dojo Foundation <http://dojofoundation.org/>
//  Based on Underscore.js, copyright 2009-2015 Jeremy Ashkenas,
//    DocumentCloud and Investigative Reporters & Editors <http://underscorejs.org/>
//
//  Permission is hereby granted, free of charge, to any person obtaining
//  a copy of this software and associated documentation files (the
//  "Software"), to deal in the Software without restriction, including
//  without limitation the rights to use, copy, modify, merge, publish,
//    distribute, sublicense, and/or sell copies of the Software, and to
//  permit persons to whom the Software is furnished to do so, subject to
//  the following conditions:
//
//    The above copyright notice and this permission notice shall be
//  included in all copies or substantial portions of the Software.
//
//    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
//    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
//  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
//  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
//  LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
//  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
//  WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

  var _ = (function() {
    var reIsDeepProp = /\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/,
      reIsPlainProp = /^\w*$/,
      rePropName = /[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]/g,
      reEscapeChar = /\\(\\)?/g,
      reIsUint = /^(?:0|[1-9]\d*)$/,
      reIsBadHex = /^[-+]0x[0-9a-f]+$/i,
      reIsBinary = /^0b[01]+$/i,
      reIsOctal = /^0o[0-7]+$/i;

    var argsTag = '[object Arguments]',
      stringTag = '[object String]',
      funcTag = '[object Function]',
      genTag = '[object GeneratorFunction]';

    var INFINITY = 1 / 0,
      MAX_SAFE_INTEGER = 9007199254740991,
      MAX_INTEGER = 1.7976931348623157e+308,
      NAN = 0 / 0;

    var FUNC_ERROR_TEXT = 'Expected a function';

    function _findIndex(array, property, value) {
      var predicate = function(item, i, arr) {
        return item[property] === value;
      };
      return _findIndexPredicate(array, predicate);
    }

    function _get(object, path, defaultValue) {
      var result = object == null ? undefined : baseGet(object, path);
      return result === undefined ? defaultValue : result;
    }

    function baseHas(object, key) {
      // Avoid a bug in IE 10-11 where objects with a [[Prototype]] of `null`,
      // that are composed entirely of index properties, return `false` for
      // `hasOwnProperty` checks of them.
      return Object.prototype.hasOwnProperty.call(object, key) ||
        (typeof object == 'object' && key in object && Object.getPrototypeOf(object) === null);
    }

    function _findIndexPredicate(array, predicate, fromRight) {
      var length = array.length,
        index = fromRight ? length : -1;

      while ((fromRight ? index-- : ++index < length)) {
        if (predicate(array[index], index, array)) {
          return index;
        }
      }
      return -1;
    }

    function isKey(value, object) {
      if (typeof value == 'number') {
        return true;
      }
      return !Array.isArray(value) &&
        (reIsPlainProp.test(value) || !reIsDeepProp.test(value) ||
        (object != null && value in Object(object)));
    }

    function isObjectLike(value) {
      return !!value && typeof value == 'object';
    }

    function isObject(value) {
      // Avoid a V8 JIT bug in Chrome 19-20.
      // See https://code.google.com/p/v8/issues/detail?id=2291 for more details.
      var type = typeof value;
      return !!value && (type == 'object' || type == 'function');
    }

    function _isFunction(value) {
      // The use of `Object#toString` avoids issues with the `typeof` operator
      // in Safari 8 which returns 'object' for typed array constructors, and
      // PhantomJS 1.9 which returns 'function' for `NodeList` instances.
      var tag = isObject(value) ? Object.prototype.toString.call(value) : '';
      return tag == funcTag || tag == genTag;
    }

    function isLength(value) {
      return typeof value == 'number' && value > -1 && value % 1 == 0 && value <= MAX_SAFE_INTEGER;
    }
    function isString(value) {
      return typeof value == 'string' ||
        (!Array.isArray(value) && isObjectLike(value) && Object.prototype.toString.call(value) == stringTag);
    }

    function isArrayLikeObject(value) {
      return isObjectLike(value) && isArrayLike(value);
    }

    function isArrayLike(value) {
      return value != null &&
        !(typeof value == 'function' && isFunction(value)) && isLength(getLength(value));
    }

    function isIndex(value, length) {
      value = (typeof value == 'number' || reIsUint.test(value)) ? +value : -1;
      length = length == null ? MAX_SAFE_INTEGER : length;
      return value > -1 && value % 1 == 0 && value < length;
    }

    function isArguments(value) {
      // Safari 8.1 incorrectly makes `arguments.callee` enumerable in strict mode.
      return isArrayLikeObject(value) && Object.prototype.hasOwnProperty.call(value, 'callee') &&
        (!Object.prototype.propertyIsEnumerable.call(value, 'callee') || Object.prototype.toString.call(value) == argsTag);
    }

    function isPrototype(value) {
      var Ctor = value && value.constructor,
        proto = (typeof Ctor == 'function' && Ctor.prototype) || Object.prototype;

      return value === proto;
    }

    function isSpace(charCode) {
      return ((charCode <= 160 && (charCode >= 9 && charCode <= 13) || charCode == 32 || charCode == 160) || charCode == 5760 || charCode == 6158 ||
      (charCode >= 8192 && (charCode <= 8202 || charCode == 8232 || charCode == 8233 || charCode == 8239 || charCode == 8287 || charCode == 12288 || charCode == 65279)));
    }

    function baseGet(object, path) {
      path = isKey(path, object) ? [path + ''] : baseToPath(path);

      var index = 0,
        length = path.length;

      while (object != null && index < length) {
        object = object[path[index++]];
      }
      return (index && index == length) ? object : undefined;
    }

    function baseToPath(value) {
      return Array.isArray(value) ? value : stringToPath(value);
    }

    function stringToPath(string) {
      var result = [];
      string.toString().replace(rePropName, function(match, number, quote, string) {
        result.push(quote ? string.replace(reEscapeChar, '$1') : (number || match));
      });
      return result;
    }

    function trimmedStartIndex(string) {
      var index = -1,
        length = string.length;

      while (++index < length && isSpace(string.charCodeAt(index))) {}
      return index;
    }

    function trimmedEndIndex(string) {
      var index = string.length;

      while (index-- && isSpace(string.charCodeAt(index))) {}
      return index;
    }

    function baseTrim(string) {
      return string
        ? string.slice(trimmedStartIndex(string), trimmedEndIndex(string) + 1)
        : string;
    }

    function toInteger(value) {
      if (!value) {
        return value === 0 ? value : 0;
      }
      value = toNumber(value);
      if (value === INFINITY || value === -INFINITY) {
        var sign = (value < 0 ? -1 : 1);
        return sign * MAX_INTEGER;
      }
      var remainder = value % 1;
      return value === value ? (remainder ? value - remainder : value) : 0;
    }

    function toNumber(value) {
      if (!value) {
        return value === 0 ? value : +value;
      }
      if (isObject(value)) {
        var other = isFunction(value.valueOf) ? value.valueOf() : value;
        value = isObject(other) ? (other + '') : other;
      }
      if (typeof value == 'number' || !isString(value)) {
        return +value;
      }
      value = baseTrim(value);
      var isBinary = reIsBinary.test(value);
      return (isBinary || reIsOctal.test(value))
        ? parseInt(value.slice(2), isBinary ? 2 : 8)
        : (reIsBadHex.test(value) ? NAN : +value);
    }

    function baseKeys(object) {
      return Object.keys(Object(object));
    }

    function indexKeys(object) {
      var length = object ? object.length : undefined;
      return (isLength(length) && (Array.isArray(object) || isString(object) || isArguments(object)))
        ? baseTimes(length, String)
        : null;
    }

    function baseTimes(n, iteratee) {
      var index = -1,
        result = Array(n);

      while (++index < n) {
        result[index] = iteratee(index);
      }
      return result;
    }

    function keys(object) {
      var isProto = isPrototype(object);
      if (!(isProto || isArrayLike(object))) {
        return baseKeys(object);
      }
      var indexes = indexKeys(object),
        skipIndexes = !!indexes,
        result = indexes || [],
        length = result.length;

      for (var key in object) {
        if (baseHas(object, key) &&
          !(skipIndexes && (key == 'length' || isIndex(key, length))) &&
          !(isProto && key == 'constructor')) {
          result.push(key);
        }
      }
      return result;
    }


    function copyObject(source, props, object) {
      return copyObjectWith(source, props, object);
    }

    function copyObjectWith(source, props, object, customizer) {
      object || (object = {});

      var index = -1,
        length = props.length;

      while (++index < length) {
        var key = props[index],
          newValue = customizer ? customizer(object[key], source[key], key, object, source) : source[key];

        assignValue(object, key, newValue);
      }
      return object;
    }

    function assignValue(object, key, value) {
      var oldValue = object[key];
      if ((value === value ? (value !== oldValue) : (oldValue === oldValue)) ||
        (value === undefined && !(key in object))) {
        object[key] = value;
      }
    }

    var _assign = createAssigner(function(object, source) {
      copyObject(source, keys(source), object);
    });

    function apply(func, thisArg, args) {
      var length = args ? args.length : 0;
      switch (length) {
        case 0: return func.call(thisArg);
        case 1: return func.call(thisArg, args[0]);
        case 2: return func.call(thisArg, args[0], args[1]);
        case 3: return func.call(thisArg, args[0], args[1], args[2]);
      }
      return func.apply(thisArg, args);
    }

    function rest(func, start) {
      if (typeof func != 'function') {
        throw new TypeError(FUNC_ERROR_TEXT);
      }
      start = Math.max(start === undefined ? (func.length - 1) : toInteger(start), 0);
      return function() {
        var args = arguments,
          index = -1,
          length = Math.max(args.length - start, 0),
          array = Array(length);

        while (++index < length) {
          array[index] = args[start + index];
        }
        switch (start) {
          case 0: return func.call(this, array);
          case 1: return func.call(this, args[0], array);
          case 2: return func.call(this, args[0], args[1], array);
        }
        var otherArgs = Array(start + 1);
        index = -1;
        while (++index < start) {
          otherArgs[index] = args[index];
        }
        otherArgs[start] = array;
        return apply(func, this, otherArgs);
      };
    }

    function isIterateeCall(value, index, object) {
      if (!isObject(object)) {
        return false;
      }
      var type = typeof index;
      if (type == 'number'
          ? (isArrayLike(object) && isIndex(index, object.length))
          : (type == 'string' && index in object)) {
        var other = object[index];
        return value === value ? (value === other) : (other !== other);
      }
      return false;
    }

    function createAssigner(assigner) {
      return rest(function(object, sources) {
        var index = -1,
          length = object == null ? 0 : sources.length,
          customizer = length > 1 ? sources[length - 1] : undefined,
          guard = length > 2 ? sources[2] : undefined;

        customizer = typeof customizer == 'function' ? (length--, customizer) : undefined;
        if (guard && isIterateeCall(sources[0], sources[1], guard)) {
          customizer = length < 3 ? undefined : customizer;
          length = 1;
        }
        object = Object(object);
        while (++index < length) {
          var source = sources[index];
          if (source) {
            assigner(object, source, customizer);
          }
        }
        return object;
      });
    }

    function baseProperty(key) {
      return function(object) {
        return object == null ? undefined : object[key];
      };
    }

    var getLength = baseProperty('length');

    function arrayFilter(array, predicate) {
      var index = -1,
        length = array.length,
        resIndex = 0,
        result = [];

      while (++index < length) {
        var value = array[index];
        if (predicate(value, index, array)) {
          result[resIndex++] = value;
        }
      }
      return result;
    }

    function baseFilter(collection, predicate) {
      var result = [];
      baseEach(collection, function(value, index, collection) {
        if (predicate(value, index, collection)) {
          result.push(value);
        }
      });
      return result;
    }

    function _filter(collection, predicate) {
      var func = Array.isArray(collection) ? arrayFilter : baseFilter;
      return func(collection, predicate);
    }

    return  {
      filter: _filter,
      findIndex: _findIndex,
      get: _get,
      assign: _assign,
      isFunction: _isFunction
    };

  })();

  //////////////////////////// end of copied from lodash //////////////////////////////

  return RemoteModelInterface;
});
