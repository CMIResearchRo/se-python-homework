"""
    Create 3 classes:
        - Cat
        - Dog
        - Mouse

    All of these 3 classes must inherit from the Animal class.

    public attributes:
        - inherited from Animal (on init (or also called constructor))
        - enemy (on constructor (init))
            - is reference to the enemy of the current Animal
            e.g. Dog is the enemy of Cat

    private attributes:
        - specific_sound: str

    public methods:
        - inherited from Animal

    private methods:
        - enemy_fear_sound() - returns str
            - this is called inside the sound() method, and if an enemy has
            been passed on the constructor, then the sound should be different
            than the usual sound of the animal

            e.g.
                if Cat is called with enemy = Dog, then the cat should make
            a "meoooooow scared" sound.
                else the cat makes a "meow" sound
"""