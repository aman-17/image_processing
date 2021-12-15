
(function() {
    // This is for older iAd proprietary bundles that may try to access
    // bindings previously exposed on the banner object.
    window.banner = {};
    // We're not suppoting these events. Good code would check the existence
    // of these events before adding an event listener. In this case, set
    // the event to null, to indicate that the event is not supported.
    window.DeviceMotionEvent = null;
    window.DeviceOrientationEvent = null;

    var nativeAddEventListener = window.EventTarget.prototype.addEventListener;

    // Swizzle out addEventListener and throw an error if we don't want to support the event.
    window.EventTarget.prototype.addEventListener = function (event, callback, useCapture) {
        if (event == "deviceorientation" || event == "devicemotion") {
            throw new Error("The " + event + " event is not supported in this advertisement.");
        }
        // Otherwise, call back to the native implementation.
        nativeAddEventListener.call(this, event, callback, useCapture);
    }

    window.navigator.geolocation.getCurrentPosition = function (showLocation, errorHandler, options) {
        throw new Error("The geolocation API 'getCurrentPosition()' is not supported in this advertisement.");
    }

    window.navigator.geolocation.watchPosition = function (showLocation, errorHandler, options) {
        throw new Error("The geolocation API 'watchPosition()' is not supported in this advertisement.");
    }

    window.navigator.geolocation.clearWatch = function (watchId) {
        throw new Error("The geolocation API 'clearWatch()' is not supported in this advertisement.");
    }

})();
