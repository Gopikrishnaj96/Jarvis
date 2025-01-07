$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync:true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect:"bounceOut",

        },
    });
    //Siri config
    
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 810,
        height: 250,
        style:"ios9",
        speed:0.3,
        amplitude:"1",
        autostart:true
    });
    //siri msg animation
    $('.siri-message').textillate({
        loop: true,
        sync:true,
        in:{
            effect: "fadeInUp",
            sync:true
        },
        out:{
            effect:"fadeOutUp",
            sync:true,
        },
    });
    $("#MicBtn" ).click(function () { 
        //eel.playAssistandSound()
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false)
        
    });
});