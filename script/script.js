var result;
var user, computer, url;
var serverAadress="http://dijkstra.cs.ttu.ee/~Alar.Laanep"
var $name=$("#name").val();
$(document).ready(function() {
	$('button[type="submit"]').prop('disabled', true);
    $('#name').keyup(function() {
        var disable = false;

        $('#name').each(function() {
        	if($(this).val() == '') { disable = true };
        });

        $('button[type="submit"]').prop('disabled', disable);
        $name=$("#name").val();
        sessionStorage.name=$name;
    		
    });
});

$("#startGameAgainstComputer").click(function(){
	//alert("Handler for click() called.");
	//window.location.assign("http://dijkstra.cs.ttu.ee/~Alar.Laanep/prax3/game.html");
});	



//player object constructor
function Player(move, a_name, moves, score, round, result){
	this.move=move;	//players move rock, paper, scissors
	this.name=a_name; //player name
	this.score=score; //player overall score
	this.round=round; //game round
	this.result=result;

	//get score
	Player.prototype.getScore=function(){
		return this.score;
	};

	//get rounds
	Player.prototype.getRounds=function(){
		return this.round;
	};

	//get player Name
	Player.prototype.getUserName=function(){
		return this.name;
	};
};


//initialize user and computer objects
function init(){
	user=new Player("", 'Player', [],0, 0);
	computer=new Player("", 'Computer', [], 0, 0); 
	user.name=sessionStorage.name;
	console.log(user.name)
	document.getElementById('playerHeading').innerHTML=user.getUserName();
	document.getElementById('userImage').src=serverAadress+'/prax3/img/chooseyourweapon.png';
	document.getElementById('computerImage').src=serverAadress+'/prax3/img/chooseyourweapon.png';
	//document.getElementById('result').innerHTML='0';
	document.getElementById('rounds').innerHTML=user.getRounds();
    document.getElementById('playerScore').innerHTML=user.getScore();
    document.getElementById('computerScore').innerHTML=computer.getScore(); 
    $(function(){
		$.ajax({
			url: serverAadress+'/cgi-bin/prax3/deleteFromFile.py',
			type: 'post',
			data: JSON.stringify({'param':{"success":"success"}}),
			dataType:'json',
			success: function(response){
				console.log('Success')				
			}
		});
	});
}

$(document).ready(function(){
    $(".userChoice").click(function(){
    	//get user choice from button clicked
        user.move=$(this).val();
       
        $(function(){
			$.ajax({
				url: serverAadress+'/cgi-bin/prax3/script.py',
				type: 'post',
				data: JSON.stringify({'param':{"usermove": user.move, 'username':user.name}}),
				dataType:'json',
				success: function(response){
					user.move=response['usermove'];
					computer.move= response['computermove'];
					result=response['result'];
					user.score=response['userscore'];
					computer.score=response['computerscore'];
					user.round=response['userround'];
					//change user img accordingly to user choice
        			document.getElementById('userImage').src=serverAadress+'/prax3/img/'+user.move+'.png'
        			//change computer img accordingly to computer choice
					document.getElementById('computerImage').src=serverAadress+'/prax3/img/'+computer.move+'.png'
        			document.getElementById('rounds').innerHTML=user.round;
        			document.getElementById('playerScore').innerHTML=user.score;
        			document.getElementById('computerScore').innerHTML=computer.score;
        			//document.getElementById('result').innerHTML=result;
        			$("<span class='results'>"+result+"</span><br>").insertAfter('#result'); 
        			var list=document.getElementById("res");
        				if (list.hasChildNodes()) {
        					if(list.childNodes[7]){
        						list.removeChild(list.childNodes[7]);
        					}    						
						}
					
				}
			});
		});
	});        
});

function ShowScore(){
	$(function(){
		$.ajax({
			url: serverAadress+'/cgi-bin/prax3/scores.py',
			type: 'post',
			data: JSON.stringify({'param':{"success":"success"}}),
			dataType:'json',
			success: function(response){
				console.log(response);			
			}
		});
	});
} 



