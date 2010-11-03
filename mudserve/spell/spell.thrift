namespace py mudserve.mudrpc.spell
include "spell_types.thrift"
include "../auth/auth_types.thrift"

service SpellService {
	list<spell_types.Spell> getSpells(1: auth_types.AuthToken authToken)
	  throws (1: auth_types.MUDAUserException userException,
			  2: auth_types.MUDASystemException systemException)
}
