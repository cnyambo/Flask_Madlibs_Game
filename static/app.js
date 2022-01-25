verb =  document.getElementById("verb").value
place =  document.getElementById("place").value
noun = $("#noun")
adj = $("#noun")
plural = $("#plural")

function valid_data()
{
	if(verb.length < 3 )
		alert("the inputs verb should have at least 3 char")
		//window.location = '/';	
	else if ( place.length <3 )
		alert("the inputs place should have at least 3 char")
		//window.location = '/';

}

