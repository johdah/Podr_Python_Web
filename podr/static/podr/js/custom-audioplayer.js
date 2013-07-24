// Constants
const PODR_EPISODE_ID = "podr.current.episode.id";
const PODR_EPISODE_TITLE = "podr.current.episode.title";
const PODR_ENCLOSURE_TIME = "podr.current.enclosure.time";
const PODR_ENCLOSURE_TYPE = "podr.current.enclosure.type";
const PODR_ENCLOSURE_URL = "podr.current.enclosure.url";

var playerAudioElement = new Audio();

jQuery(document).ready(function(){
    container = $('#player-controls');
    cover = $('#player-controls .cover');
    play = $('#player-controls #play');
    pause = $('#player-controls #pause');
    mute = $('#player-controls #mute');
    muted = $('#player-controls #muted');
    close = $('#player-controls #close');
    playerAudioElement = new Audio();

    playerAudioElement.type= localStorage[PODR_ENCLOSURE_TYPE];
    playerAudioElement.src= localStorage[PODR_ENCLOSURE_URL];
    duration = playerAudioElement.duration;

    // TODO: Turn autoplay off
    playerAudioElement.play();


    play.live('click', function(e) {
        e.preventDefault();
        playerAudioElement.play();

        $(this).replaceWith('<a class="button gradient" id="pause" href="" title=""></a>');
        container.addClass('containerLarge');
        cover.addClass('coverLarge');
        $('#close').fadeIn(300);
        $('#seek').attr('max',playerAudioElement.duration);
    });

    pause.live('click', function(e) {
        e.preventDefault();
        playerAudioElement.pause();
        $(this).replaceWith('<a class="button gradient" id="play" href="" title=""></a>');

    });

    mute.live('click', function(e) {
        e.preventDefault();
        playerAudioElement.volume = 0;
        $(this).replaceWith('<a class="button gradient" id="muted" href="" title=""></a>');

    });

    muted.live('click', function(e) {
        e.preventDefault();
        playerAudioElement.volume = 1;
        $(this).replaceWith('<a class="button gradient" id="mute" href="" title=""></a>');

    });

    $('#close').click(function(e) {
        e.preventDefault();
        container.removeClass('containerLarge');
        cover.removeClass('coverLarge');
        playerAudioElement.pause();
        playerAudioElement.currentTime = 0;
        $('#pause').replaceWith('<a class="button gradient" id="play" href="" title=""></a>');
        $('#close').fadeOut(300);
    });



    $("#seek").bind("change", function() {
        playerAudioElement.currentTime = $(this).val();
        $("#seek").attr("max", playerAudioElement.duration);
    });

    playerAudioElement.addEventListener('timeupdate',function (){
        curtime = parseInt(playerAudioElement.currentTime, 10);
        $("#seek").attr("value", curtime);
    });
});



// TODO: Fix save current episode to localStorage
// TODO: Fix save current time to localStorage
// TODO: Support for more fileTypes than mp3
/*$(document).ready(function(){
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
});*/

// TODO: Does this work?
function loadEpisode() {
    episodeId = $('#episode_id').text();
    episodeTitle = $('#episode_title').text();
    enclosureUrl = $('#enclosure_url').text();
    enclosureType = $('#enclosure_type').text();

    playerAudioElement.src = enclosureUrl;
    playerAudioElement.type = enclosureType;
    playerAudioElement.play();

    //$("#playing_episode_title").text(episodeTitle);

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
/*function loadPlayerState() {
    if (!Modernizr.localstorage) { return false; }
    if( localStorage[PODR_ENCLOSURE_URL]) {
        $("#audio-player-container").jPlayer("setMedia", {
            mp3: localStorage[PODR_ENCLOSURE_URL]
        });

        $("#audio-player-container").bind($.jPlayer.event.canplaythrough, function() {
            //$("#audio-player-container").jPlayer("play", localStorage[PODR_ENCLOSURE_TIME]);
            // TODO: Autoplay disabled
            //$("#audio-player-container").jPlayer("play");
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
}*/