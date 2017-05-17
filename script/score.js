var serverAadress="http://dijkstra.cs.ttu.ee/~Alar.Laanep";
var myData;
var $name, $date;

function showScore(){
	$(function(){
		console.log('i run');
		$name=$('#name');
		$date=$('#date');
		$.ajax({
			url: serverAadress+'/cgi-bin/prax3/scores.py',
			type: 'post',
			data: JSON.stringify({'param':{"name":$name.val(), 'date':$date.val()}}),
			dataType:'json',
			success: function(response){
				$('table tbody').empty();
				myData=response;
				var tr;
				if (myData['rounds'].length==0){
					document.getElementById('noData').innerHTML='Sorry, no data to show. Try to search again!';
					$('table').hide()
				}
				for (var i=0; i<myData['rounds'].length; i++){
					tr=$('<tr/>');
					tr.append("<td>"+myData['rounds'][i].time+"</td>");
					tr.append("<td>"+myData['rounds'][i].playername+"</td>");
					tr.append("<td>"+myData['rounds'][i].userround+"</td>");
					tr.append("<td>"+myData['rounds'][i].usermove+'/'+myData['rounds'][i].computermove+"</td>");
					tr.append("<td>"+myData['rounds'][i].result+"</td>");
					tr.append("<td>"+myData['rounds'][i].userscore+'/'+myData['rounds'][i].computerscore+"</td>");
					$('table').append(tr);
				}
			}
		});
	});
} 