function showMenu(event){
    const navbarLinks = $(".navbar-links")[0];
    navbarLinks.classList.toggle("active");
}

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
    $("#selected-image").css("border-radius","4px"); 

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
    let server_url = "http://127.0.0.1:5000";
    let api = "/cxra/predict";
    $.post(server_url + api, JSON.stringify(body), function(response){
        let prediction = response.data.result;
        let percentage = response.data.accuracy * 100;
        percentage = percentage.toFixed();
        $(".result").text(percentage +"% chances of Covid " + prediction);
        $("#predict-button").css("visibility","hidden");
        $(".result").css("visibility","visible");
    });
});

$("#train-button").click(function(){
    let epoch = $(".inputBox .text")[1].value;
    let server_url = "http://127.0.0.1:5000";
    let api = "/train_model";
    let rawText = $(".training-time").text();
    let device = rawText.substr(25,3);
    let totalTime = 0;
    if(device == "GPU"){
        totalTime = (epoch*3) + 2;
    }
    else{
        totalTime = (epoch*30) + 2;
    }
    let trainingSession = "";
    if(epoch>1){
        trainingSession = " for " +epoch +" training sessions is ";
    }else{
        trainingSession = " for " +epoch +" training session is ";
    }
    let trainingText = rawText + trainingSession;
    if(totalTime > 60){
        totalTime = totalTime/60;
        totalTime = totalTime.toFixed()
        trainingText += totalTime + " hours."
    }else{
        trainingText += totalTime + " minutes."
    }
    $(".inputBox").css("visibility","hidden");
    $("#train-button").css("visibility","hidden");
    $(".training-time").text(trainingText);
    $(".training-time").css("visibility","visible");
    $(".container-progress-bar").css("visibility","visible");
    $.post(server_url + api,JSON.stringify({"epochs":epoch}), function(response){
        console.log(response);
        $(".training-time").css("visibility","visible");
        $(".container-progress-bar").css("visibility","hidden");
        $(".training-time").css("visibility","hidden");
        $(".result").text("Model Trained!");
        $(".result").css("visibility","visible");
        
    });
});
   