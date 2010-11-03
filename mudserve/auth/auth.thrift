namespace py mudserve.mudrpc.auth

/**
 * This contains the authentication format for the MudServe server.
 * This is heavily inspired by Evernote's EDAM protocol.
 * Our implementation of the protocol will be called MUDA.
 */

include "auth_types.thrift"

// Major version number of authentication protocol
const i16 MUDA_VERSION_MAJOR = 0
// Minor version number of authentication protocol
const i16 MUDA_VERSION_MINOR = 1

struct AuthenticationResult {
	1: required auth_types.Timestamp currentTime,
	2: required auth_types.AuthToken authToken,
	3: required auth_types.Timestamp expirationTime,
	4: optional auth_types.User user
}

service UserAuth {
	/**
	 * Makes sure the client is up to date.
	 *
	 * @param clientName
	 *   This should provide some information about the client,
	 *   of the format:
	 *   application/version; platform/version
	 *   For example "MUDA iOS/1.0.0; iOS/4.0"
	 *
	 * @param mudaVersionMajor
	 *   The major version of the client.
	 *
	 * @param mudaVersionMinor
	 *   The minor version of the client.
	 */
	bool checkVersion(1: string clientName,
	                  2: i16 mudaVersionMajor = MUDA_VERSION_MAJOR,
					  3: i16 mudaVersionMinor = MUDA_VERSION_MINOR),

	/**
	 * Checks that the username and password are okay in order to properly
	 * authenticate the user.
	 *
	 * @param username
	 *   The username for the account to authenticate with. This should likely
	 *   be the user's email address.
	 *
	 * @param password
	 *   The password (TODO: decide whether to use plaintext or hashed) of the
	 *   client to authenticate with.
	 *
	 * @return
	 *   The result of the successful authentication. This will be an
	 *   AuthenticationResult object.
	 *
	 * @throws MUDAUserException
	 *   - DATA_REQUIRED "username" - Username is empty
	 *   - DATA_REQUIRED "password" - Password is empty
	 *   - INVALID_AUTH  "username" - Username not found
	 *   - INVALID_AUTH  "password" - Password mismatch
	 *   - PERMISSION_DENIED "User.active" - User account is closed
	 */
	AuthenticationResult authenticate(1: string username, 2: string password)
	  throws (1: auth_types.MUDAUserException userException,
	          2: auth_types.MUDASystemException systemException),
	
	/**
	 * Exchanges an authentication token for a newer one which will not
	 * expire as soon. This cannot be used on an expired token.
	 * @param authToken
	 *   The previously used authentication token.
	 *
	 * @return
	 *   Returns a new AuthenticationResult, where the user field will not be
	 *   available.
	 */
	AuthenticationResult refreshToken(1: auth_types.AuthToken authToken)
	  throws (1: auth_types.MUDAUserException userException,
	          2: auth_types.MUDASystemException systemException)
	
}
