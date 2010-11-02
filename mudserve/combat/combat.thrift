struct Fight {
	1: i32  id,
	2: byte turn,
}

service FightService {
	int castSpell(1:i32 spell, 2:i32 target)
}
