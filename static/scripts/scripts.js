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
function addBorder(event){
    $("#selected-image").css("border","3px solid #F2F2F8"); 
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
    let body = {
        image: base64Image
    }
    let server_url = "http://127.0.0.1:5000"
    let api = "/predict"
    $.post(server_url + api, JSON.stringify(body), function(response){
        let prediction = response.data.result;
        let percentage = response.data.accuracy.toFixed(2)*100;
        $(".result").text(percentage +"% chances of " + prediction);
        $("#predict-button").css("visibility","hidden");
        $(".result").css("visibility","visible");
    });
});

$("#train-button").click(function(){
    let server_url = "http://127.0.0.1:5000"
    let api = "/train_model"
    $.post(server_url + api,JSON.stringify({}), function(response){
        console.log(response);
    });
});
   