// Constants
const PODR_EPISODE_ID = "podr.current.episode.id";
const PODR_EPISODE_TITLE = "podr.current.episode.title";
const PODR_ENCLOSURE_TIME = "podr.current.enclosure.time";
const PODR_ENCLOSURE_TYPE = "podr.current.enclosure.type";
const PODR_ENCLOSURE_URL = "podr.current.enclosure.url";

// TODO: Fix save current episode to localStorage
// TODO: Fix save current time to localStorage
// TODO: Support for more fileTypes than mp3
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
        },
        timeupdate: function(event) { // 4Hz
            saveCurrentState(event);
        }
    });
});

// TODO: Does this work?
// TODO: Support more filetypes
function loadEpisode() {
    episodeId = $('#episode_id').text();
    episodeTitle = $('#episode_title').text();
    enclosureUrl = $('#enclosure_url').text();
    enclosureType = $('#enclosure_type').text();

    $("#audio-player-container").jPlayer("setMedia", {
        mp3: enclosureUrl
    });

    $("#playing_episode_title").text(episodeTitle)

    if (!Modernizr.localstorage) { return false; }
    localStorage[PODR_EPISODE_ID] = episodeId;
    localStorage[PODR_EPISODE_TITLE] = episodeTitle;
    localStorage[PODR_ENCLOSURE_TIME] = 0;
    console.log("Reset current enclosure time!");
    localStorage[PODR_ENCLOSURE_TYPE] = enclosureType;
    localStorage[PODR_ENCLOSURE_URL] = enclosureUrl;
}

// TODO: Fix load latest episode from localStorage
// TODO: Fix load current time to localStorage
// TODO: Support for more fileTypes than mp3
// TODO: Need support for Modernizer
function loadPlayerState() {
    if (!Modernizr.localstorage) { return false; }
    if( localStorage[PODR_ENCLOSURE_URL]) {
        $("#audio-player-container").jPlayer("setMedia", {
            mp3: localStorage[PODR_ENCLOSURE_URL]
        });

        $("#audio-player-container").bind($.jPlayer.event.canplaythrough, function() {
            //$("#audio-player-container").jPlayer("play", localStorage[PODR_ENCLOSURE_TIME]);
            $("#audio-player-container").jPlayer("play");
            console.log("Loading enclosure time: " + localStorage[PODR_ENCLOSURE_TIME]);
            $('#playing_episode_title').text(localStorage[PODR_EPISODE_TITLE]);
        });
    }
    else {
        $('#playing_episode_title').text("No episode");
    }
}

function saveCurrentState(event) {
    if (!Modernizr.localstorage) { return false; }
    //if(event.jPlayer.status.paused) { return false; }

    //if(event.jPlayer.status.ended) // TODO: Mark episode as finished
    if (event.jPlayer.status.currentTime > 1) { // TODO: Run less often
        localStorage[PODR_ENCLOSURE_TIME] = event.jPlayer.status.currentTime;
        console.log("Saving enclosure time: " + localStorage[PODR_ENCLOSURE_TIME]);
        $("#audio-controls-seekbar .bar").css("width", event.jPlayer.status.currentPercentAbsolute + "%");
    }
}