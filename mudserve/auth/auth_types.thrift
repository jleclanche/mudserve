namespace py mudserve.mudrpc.auth.types

/**
 * A timestamp expressed as the number of milliseconds since the standard epoch
 *
 *     January 1, 1970, 00:00:00 GMT
 *
 * This is expressed with a precision of seconds, so the last three digits
 * representing milliseconds will be '000'.
 *
 * Since Thrift does not specify a datetime type, we use this instead.
 */
typedef i64 Timestamp

// User ID type
typedef i32 UserID

// Auth token type
typedef string AuthToken

/**
 * The User structure.
 * All fields are optional because what is set will depend on the context.
 */
struct User {
	1: optional UserID id,
	2: optional string username,
	3: optional bool active,
	4: optional Timestamp created,
	5: optional Timestamp deleted,
}

/**
 * Various error codes used by all error messages.
 * - UNKNOWN
 *     No error information available.
 * - BAD_DATA_FORMAT
 *     The data request was malformatted.
 * - INTERNAL_ERROR
 *     An unexpected internal problem has occurred.
 * - DATA_REQUIRED
 *     A required parameter was not found in the request.
 * - PERMISSION_DENIED
 *     The requested action is not allowed.
 * - INVALID_AUTH
 *     The authentication information provided was incorrect.
 * - AUTH_EXPIRED
 *     The authentication token has expired.
 */
 
enum MUDAErrorCode {
	UNKNOWN = 1,
	BAD_DATA_FORMAT = 2,
	INTERNAL_ERROR = 3,
	DATA_REQUIRED = 4,
	PERMISSION_DENIED = 5,
	INVALID_AUTH = 6,
	AUTH_EXPIRED = 7
}

/**
 * This exception is thrown when the error is on the user's side and may be
 * resolvable by altering the procedure.
 */
exception MUDAUserException {
	1: required MUDAErrorCode errorCode,
	2: optional string parameter
}

/**
 * This exception is thrown when the error occurred because of a problem
 * with the service rather than that of the user or client, and is not
 * resolvable by altering the procedure.
 */
exception MUDASystemException {
	1: required MUDAErrorCode errorCode,
	2: optional string message
}
