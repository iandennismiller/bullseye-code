var ctx, img;
var state = "up";
var x0, y0, x1, y1;

var update_image = function() {
    var canvas = document.getElementById('image');
    if (canvas && canvas.getContext) {
        ctx = canvas.getContext('2d');
    }

    img = new Image();
    img.onload = function() {
        ctx.drawImage(img, 350, 1200, 1870, 1900, 0, 0, 800, 800);
    };

    img.src = '/images/l0000.png';
    ctx.lineWidth = 3;

    $("#image").click(function(e) {
        var x = e.pageX - this.offsetLeft;
        var y = e.pageY - this.offsetTop;
        console.log("" + x + " " + y);

        if (state == "up") {
            x0 = x;
            y0 = y;
            state = "down";
        }
        else if (state == "down") {
            x1 = x;
            y1 = y;            
            state = "up";
            ctx.beginPath();
            ctx.moveTo(x0, y0);
            ctx.lineTo(x1, y1);
            ctx.closePath();
            ctx.stroke();
        }
    });
};
