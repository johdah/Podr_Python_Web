// TODO: Fix save current episode to localStorage
// TODO: Fix save current time to localStorage
$(document).ready(function(){
    $("#audio-player-container").jPlayer({
        ready: function () {
            loadPlayerState();
        },
        swfPath: "/js",
        supplied: "mp3",
        cssSelectorAncestor: "",
        cssSelector: {
            play: "#play",
            pause: "#pause",
            stop: "#stop",
            mute: "#mute",
            unmute: "#unmute",
            currentTime: "#currentTime",
            duration: "#duration"
        },
        size: {
            width: "0px",
            height: "0px"
        }
    });
});

// TODO: Fix load latest episode from localStorage
// TODO: Fix load current time to localStorage
function loadPlayerState() {
    if (!Modernizr.localstorage) { return false; }

    $("#audio-player-container").jPlayer("setMedia", {
        mp3: "http://www.jplayer.org/audio/mp3/Miaow-snip-Stirring-of-a-fool.mp3"
    });

    /*if(localStorage.getItem("bar")) {
        $(this).jPlayer("setMedia", {
            mp3: "http://www.jplayer.org/audio/mp3/Miaow-snip-Stirring-of-a-fool.mp3"
        })//.jPlayer("play");
    }*/
}