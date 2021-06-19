let base64Image;
var loadFile = function(event){
    let image = $("#selected-image");
    image.src = URL.createObjectURL(event.target.files[0]);
    image.onload = function() {
        URL.revokeObjectURL(image.src) // free memory
      }
      $(".result").css("visibility","hidden")
      $(".button").css("visibility","visible");

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
    let prediction = response.prediction.result;
    let percentage = response.prediction.accuracy.toFixed(2)*100;
    $(".result").text(percentage +"% chances of " + prediction);
    $(".button").css("visibility","hidden");
    $(".result").css("visibility","visible");
    console.log()
    //$(".probability").text(response.prediction.accuracy.toFixed(2));
    console.log(response);
    });
});

   