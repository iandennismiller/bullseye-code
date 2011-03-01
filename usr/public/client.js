/*
(c) 2011 Ian Dennis Miller
http://bullseye-code.googlecode.com
*/

var canvas, ctx, img, current_id;
var state = "up";
var x0, y0, x1, y1;

var handle_clicks = function(e) {
    var x = e.pageX - this.offsetLeft;
    var y = e.pageY - this.offsetTop;

    if (state == "up") {
        x0 = x;
        y0 = y;
        state = "down";
        ctx.beginPath();
        ctx.arc(x0,y0,3,0,Math.PI*2,true);
        ctx.closePath();
        ctx.fill();
    }
    else if (state == "down") {
        x1 = x;
        y1 = y;            
        state = "waiting";
        ctx.beginPath();
        ctx.moveTo(x0, y0);
        ctx.lineTo(x1, y1);
        ctx.closePath();
        ctx.stroke();
        $("#input_box").css('left', x+20);
        $("#input_box").css('top', y-20);
        $("#input_box").fadeIn();
        $("#text_input").focus();
    }
    $("#status").html(state);
};

var handle_keypress = function(e) {
    if (!e) { e=window.event; }
    switch (e.keyCode) {
        case 27:
            if (state == "down") {
                state = "up";
                ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
                ctx.beginPath();
                ctx.arc(x0,y0,3,0,Math.PI*2,true);
                ctx.closePath();
                ctx.fill();
                ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
            }
            else if (state == "waiting") {
                $("#input_box").fadeOut();
                state = "up";
            }
            break;
        case 13:
            if (state == "waiting") {
                var value = $("#text_input").val();
                var x_mid = (x0+x1) / 2;
                var y_mid = (y0+y1) / 2;
                var xd = x_mid - 400;
                var yd = y_mid - 400;
                var dist = Math.sqrt((xd*xd) + (yd*yd));
                var msg = "<span class='word'>" + value + "</span>";
                msg += "<span class='dist'>" + $.sprintf("%0.3f", dist) + "</span>";
                $("#data_table").append("<div>" + msg + "</div>");
                $("#input_box").fadeOut();
                $("#text_input").val("");
                state = "up";                    
            }
            break;
    }
    $("#status").html(state);
};

var next_image = function() {
    $.ajax({
        type: "GET",
        url: "/rpc/next_image",
        dataType: "json",
        success: next_image_cb
    });        
};

var next_image_cb = function(data) {
    if (data.id != undefined) {
        img = new Image();
        img.onload = function() {
            ctx.drawImage(img, 350, 1200, 1870, 1900, 0, 0, 800, 800);
        };
        img.src = data.filename;
        current_id = data.id;
    }
    else {
        $("#status").html("no more images");
        ctx.fillRect(0, 0, 800, 800);
    }
};

var submit_data = function() {
    // get all items in data_table
    var data = "";
    var entries = $("#data_table").children();

    for (var i = 0; i < entries.length; i++) {
        var entry = entries[i];
        var values = $(entry).children();
        var word = $(values[0]).text();
        var dist = $(values[1]).text();
        //console.log(word);
        data += word + "\t" + dist + "\t";
    }

    // submit it with ajax
    $.ajax({
        type: "POST",
        data: {
            "id": current_id,
            "data": data
        },
        url: "/rpc/store_data",
        dataType: "json",
        success: next_image
    });

    $("#data_table").html("");
}

var start = function() {
    canvas = document.getElementById('image');
    if (canvas && canvas.getContext) {
        ctx = canvas.getContext('2d');
    }
    ctx.lineWidth = 3;
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.5)';
    ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';

    next_image();
    $("#image").click(handle_clicks);
    $(window).keydown(handle_keypress);
    $("#main_control").click(submit_data);
}
