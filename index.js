'use strict';
console.log('Loading function');
let response = require('cfn-response');
let doc = require('dynamodb-doc');
let dynamo = new doc.DynamoDB();
exports.handler = (event, context, callback) => {
   var data1;
   console.log('Received event:', JSON.stringify(event, null, 2));
   // is a clientId passed? if yes, query on data in time series table for that client. if not, scan the check device table
   if (event.clientid) {
   // need to get data from last 5 minutes
   console.log("select data");
   console.log(event.clientid);
   let timestampRange = ((new Date()).getTime() - (300 *1000))/1000;
   console.log(timestampRange);
   var i;
  
 
   let params = {
       TableName: 'healthdata',
       KeyConditionExpression: 'clientid = :hkey and payloadtimestamp > :rkey',
       ExpressionAttributeValues: {
           ':hkey': event.clientid,
           ':rkey': timestampRange
       }
   };
   dynamo.query(params, function(err, data) {
       if (err) {console.log(err, err.stack);
           callback(null, {});
       }
       else  {   console.log(data);
       callback(null, data);
           
           
       }
   });
}


else {
let params = {
TableName: 'CheckDevice',
};
dynamo.scan(params, function(err, data) {
if (err) {console.log(err, err.stack); // an error occurred
callback(null, {});
}
else  {   console.log(data);           // successful response
callback(null, data);
}
});
}

};
