const {MessageRequest, MessageReply} = require('./calculator_pb.js');
const {Calculator} = require('./calculator_grpc_web_pb.js');

var CalculatorServicer = new Calculator('http://localhost:8080');

var request = new MessageRequest();
request.setMsg('Hello World');

CalculatorServicer.HelloWorld(request, {}, (err, response) => {
  console.log(response.getMsg());
});