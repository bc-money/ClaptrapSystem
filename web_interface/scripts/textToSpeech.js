function textToSpeech() {
	var msg = new SpeechSynthesisUtterance();
	var voices = window.speechSynthesis.getVoices();
	var text = document.getElementById("textToRead").value;
	var lan = "en-EN";

	msg.voice = voices[10];
	msg.voiceURI = "native";
	msg.volume = 5;
	msg.rate = 1;
	msg.pitch = 1; 
   msg.text = text;
   msg.lang = lan;
 
   speechSynthesis.speak(msg);	
}
