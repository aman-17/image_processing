class VideoAdUtilities
{
    constructor(videoPlayer)
    {
        this.videoPlayer = videoPlayer;
        this.playCompleted = false;
        this.videoLoaded = false;
    }

    static documentVideoPlayer()
    {
        var videoPlayers = document.getElementsByTagName("video");
        if (videoPlayers === null || videoPlayers.length === 0) {
            return null;
        }

        return videoPlayers[0];
    }

    prepareEventHandlers()
    {
        if (this.videoPlayer == null) {
            return;
        }
        // Setting event handlers.
        this.videoPlayer.addEventListener("canplay", () => {
                                     this.videoLoaded = true;
                                     videoAd.creativeViewLoaded();
                                     });
        this.videoPlayer.addEventListener("play", () => {
                                     this.playCompleted = false;
                                     videoAd.playStarted(this.videoPlayer.currentTime);
                                     });
        this.videoPlayer.addEventListener("playing", () => {
                                     this.playCompleted = false;
                                     videoAd.playResumed(this.videoPlayer.currentTime);
                                     });
        this.videoPlayer.addEventListener("timeupdate", () => {
                                     videoAd.playTimeUpdated(this.videoPlayer.currentTime);
                                     });
        this.videoPlayer.addEventListener("volumechange", () => {
                                     if (this.videoPlayer.muted) {
                                        videoAd.volumeMuted();
                                     } else {
                                        videoAd.volumeChanged(this.videoPlayer.volume);
                                     }
                                     });
        this.videoPlayer.addEventListener("pause", () => {
                                     videoAd.playPaused(this.videoPlayer.currentTime);
                                     });
        this.videoPlayer.addEventListener("ended", () => {
                                     this.playCompleted = true;
                                     videoAd.playCompleted(this.videoPlayer.duration);
                                     });
    }

    setPlayerAttributes()
    {
        if (this.videoPlayer == null) {
            return;
        }
        this.videoPlayer.autoplay = false;
        this.videoPlayer.muted = true;
        this.videoPlayer.loop = false;
        this.videoPlayer.controls = false;
    }
}

window.addEventListener("DOMContentLoaded", function () {
                        let videoAdUtilities = new VideoAdUtilities(VideoAdUtilities.documentVideoPlayer());
                        videoAdUtilities.setPlayerAttributes();
                        mraid.addEventListener("ready", function(event) {
                                               let videoAssetURL = videoAd.getVideoAssetURL();
                                               let videoPlayer = videoAdUtilities.videoPlayer;
                                               videoPlayer.setAttribute("src", videoAssetURL);
                                               videoAdUtilities.prepareEventHandlers();
                                               });
                        mraid.addEventListener("viewableChange", function (event) {
                                               let videoPlayer = videoAdUtilities.videoPlayer;
                                               var isViewable = mraid.isViewable();
                                               if (!isViewable && !videoPlayer.paused) {
                                                   videoPlayer.pause();
                                               } else if (!this.playCompleted && this.videoLoaded) {
                                                   videoPlayer.play();
                                               }
                                               videoAd.viewabilityChanged(isViewable);
                                               });
                        }, false);
