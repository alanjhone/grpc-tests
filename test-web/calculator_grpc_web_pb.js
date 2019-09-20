/**
 * @fileoverview gRPC-Web generated client stub for 
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!



const grpc = {};
grpc.web = require('grpc-web');

const proto = require('./calculator_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.CalculatorClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

  /**
   * @private @const {?Object} The credentials to be used to connect
   *    to the server
   */
  this.credentials_ = credentials;

  /**
   * @private @const {?Object} Options for the client
   */
  this.options_ = options;
};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.CalculatorPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

  /**
   * @private @const {?Object} The credentials to be used to connect
   *    to the server
   */
  this.credentials_ = credentials;

  /**
   * @private @const {?Object} Options for the client
   */
  this.options_ = options;
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Number,
 *   !proto.Number>}
 */
const methodDescriptor_Calculator_SquareRoot = new grpc.web.MethodDescriptor(
  '/Calculator/SquareRoot',
  grpc.web.MethodType.UNARY,
  proto.Number,
  proto.Number,
  /** @param {!proto.Number} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Number.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Number,
 *   !proto.Number>}
 */
const methodInfo_Calculator_SquareRoot = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Number,
  /** @param {!proto.Number} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Number.deserializeBinary
);


/**
 * @param {!proto.Number} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Number)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Number>|undefined}
 *     The XHR Node Readable Stream
 */
proto.CalculatorClient.prototype.squareRoot =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Calculator/SquareRoot',
      request,
      metadata || {},
      methodDescriptor_Calculator_SquareRoot,
      callback);
};


/**
 * @param {!proto.Number} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Number>}
 *     A native promise that resolves to the response
 */
proto.CalculatorPromiseClient.prototype.squareRoot =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Calculator/SquareRoot',
      request,
      metadata || {},
      methodDescriptor_Calculator_SquareRoot);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Number2,
 *   !proto.Number2>}
 */
const methodDescriptor_Calculator_Sum = new grpc.web.MethodDescriptor(
  '/Calculator/Sum',
  grpc.web.MethodType.UNARY,
  proto.Number2,
  proto.Number2,
  /** @param {!proto.Number2} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Number2.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Number2,
 *   !proto.Number2>}
 */
const methodInfo_Calculator_Sum = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Number2,
  /** @param {!proto.Number2} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Number2.deserializeBinary
);


/**
 * @param {!proto.Number2} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Number2)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Number2>|undefined}
 *     The XHR Node Readable Stream
 */
proto.CalculatorClient.prototype.sum =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Calculator/Sum',
      request,
      metadata || {},
      methodDescriptor_Calculator_Sum,
      callback);
};


/**
 * @param {!proto.Number2} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Number2>}
 *     A native promise that resolves to the response
 */
proto.CalculatorPromiseClient.prototype.sum =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Calculator/Sum',
      request,
      metadata || {},
      methodDescriptor_Calculator_Sum);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.Message,
 *   !proto.Message>}
 */
const methodDescriptor_Calculator_HelloWorld = new grpc.web.MethodDescriptor(
  '/Calculator/HelloWorld',
  grpc.web.MethodType.UNARY,
  proto.Message,
  proto.Message,
  /** @param {!proto.Message} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Message.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.Message,
 *   !proto.Message>}
 */
const methodInfo_Calculator_HelloWorld = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Message,
  /** @param {!proto.Message} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Message.deserializeBinary
);


/**
 * @param {!proto.Message} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Message)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Message>|undefined}
 *     The XHR Node Readable Stream
 */
proto.CalculatorClient.prototype.helloWorld =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Calculator/HelloWorld',
      request,
      metadata || {},
      methodDescriptor_Calculator_HelloWorld,
      callback);
};


/**
 * @param {!proto.Message} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Message>}
 *     A native promise that resolves to the response
 */
proto.CalculatorPromiseClient.prototype.helloWorld =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Calculator/HelloWorld',
      request,
      metadata || {},
      methodDescriptor_Calculator_HelloWorld);
};


module.exports = proto;

