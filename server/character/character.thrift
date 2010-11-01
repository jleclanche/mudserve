struct Character {
	1: i32 id,
	2: string name,
}

service Character {
	Character createCharacter(1:string name),
	list<Character> getCharacters(),
	void ping()
}
