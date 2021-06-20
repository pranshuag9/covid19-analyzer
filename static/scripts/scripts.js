let base64Image;
var loadFile = function(event){
    let image = $("#selected-image");
    image.src = URL.createObjectURL(event.target.files[0]);
    image.onload = function() {
        URL.revokeObjectURL(image.src) // free memory
      }
      $(".result").css("visibility","hidden");
      $("#predict-button").css("visibility","visible");  //for predict button
};

$("#image-selector").change(function() {
    let reader = new FileReader();
    reader.onload = function(e) {
        let dataURL = reader.result;
        $('#selected-image').attr("src", dataURL);
        base64Image = dataURL.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
        console.log(base64Image);
    }
    reader.readAsDataURL($("#image-selector")[0].files[0]);
    $("#result").text("");
    $("#probability").text("");
    });

$("#predict-button").click(function(){
    let message = {
        image: base64Image
    }
    console.log(message);
    $.post("http://127.0.0.1:5000/predict", JSON.stringify(message), function(response){
        let prediction = response.data.result;
        let percentage = response.data.accuracy.toFixed(2)*100;
        $(".result").text(percentage +"% chances of " + prediction);
        $("#predict-button").css("visibility","hidden");
        $(".result").css("visibility","visible");
    });
});

   