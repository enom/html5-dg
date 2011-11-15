print '''
<!-- INSERT SCRIPT INCLUDES INTO PAGE BODY -->
<script src="https://www.paypalobjects.com/js/external/dg.js"></script>
<script src="client/jquery-1.6.2.min.js" type="text/javascript"></script>
<script src="client/pptransact.js"></script>

<input type="button" onclick="bill()" value="Bill" />
<input type="button" onclick="verify()" value="Verify" />

<script>
//INITIALIZE SESSION WITH APPROPRIATE LANGUAGE
pptransact.init('py');

//CALL BILL FUNCTION TO INITIALIZE BILL
function bill(){
	pptransact.bill({
		userId:'888888',
		itemId:'123',
		itemQty:'1',
		successCallback: function(data){
			//bill success
		},
		failCallback: function(data){
			//bill cancelled 
		}
	});
}

function verify(){
	console.log('verify');
	pptransact.verify({
		userId:'888888',
		itemId:'123',
		successCallback: function(data){
			console.log('verify success');
			//verify success
		},
		failCallback: function(data){
			console.log('verify failed')
			//verify failed
		}
	});
}
</script>
'''