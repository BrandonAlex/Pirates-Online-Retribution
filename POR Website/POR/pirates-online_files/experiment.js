define(['lodash'], function (_) {
  'use strict';

  if (typeof window !== 'object') {
    return {
      isOpen: _.constant(false)
    };
  }

  var runningExperiments = _.mapKeys((window.rendererModel || window.editorModel || {}).runningExperiments, function(value, key) {
    return key.toLowerCase();
  });

  function isOpen(name) {
    return runningExperiments[name.toLowerCase()] === 'new';
  }

  return {
    isOpen: isOpen
  };
});
