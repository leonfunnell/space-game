sprites.onCreated(SpriteKind.Enemy, function (sprite) {
    sprite.setPosition(randint(0, 160), 0)
    sprite.setBounceOnWall(true)
    sprite.setVelocity(32, 18)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (sprites.allOfKind(SpriteKind.Projectile).length < maximum_bullets_on_screen) {
        bullet = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            . . . . . . 2 2 2 2 . . . . . . 
            . . . . . . 2 2 2 2 . . . . . . 
            . . . . . . 2 2 2 2 . . . . . . 
            . . . . . . 2 2 2 2 . . . . . . 
            . . . . . . 2 5 4 2 . . . . . . 
            . . . . . 2 5 4 5 5 2 . . . . . 
            . . . . . . . 5 4 . . . . . . . 
            . . . . . . . 4 5 . . . . . . . 
            `, player_rocket, 0, -71)
        music.pewPew.play()
        bullet.startEffect(effects.trail, 200)
    }
})
function Create_Player () {
    player_rocket = sprites.create(assets.image`Rocket 1`, SpriteKind.Player)
    controller.moveSprite(player_rocket)
    player_rocket.setFlag(SpriteFlag.StayInScreen, true)
    animation.runImageAnimation(
    player_rocket,
    [img`
        . . . . . . . c d . . . . . . . 
        . . . . . . . c d . . . . . . . 
        . . . . . . . c d . . . . . . . 
        . . . . . . . c b . . . . . . . 
        . . . . . . . f f . . . . . . . 
        . . . . . . . c 4 . . . . . . . 
        . . . . . . . f f . . . . . . . 
        . . . . . . . e 4 . . . . . . . 
        . . . . . . e e 5 2 . . . . . . 
        . . . . . . e 4 5 2 . . . . . . 
        . . . . . c c c 2 2 2 . . . . . 
        . . . . e e 4 4 4 5 2 2 . . . . 
        . . e f f f c c 2 2 f f 2 2 . . 
        . e e e e 2 2 4 4 4 4 5 4 2 2 . 
        e e e e e e 2 2 4 4 4 5 4 4 2 2 
        e e e e e e 2 2 4 4 4 4 5 4 2 2 
        `,img`
        . . . . . . . c d . . . . . . . 
        . . . . . . . c d . . . . . . . 
        . . . . . . . c d . . . . . . . 
        . . . . . . . c b . . . . . . . 
        . . . . . . . f f . . . . . . . 
        . . . . . . . c 3 . . . . . . . 
        . . . . . . . f f . . . . . . . 
        . . . . . . . 8 3 . . . . . . . 
        . . . . . . 8 8 1 a . . . . . . 
        . . . . . . 8 3 1 a . . . . . . 
        . . . . . c c c a a a . . . . . 
        . . . . 8 8 3 3 3 1 a a . . . . 
        . . 8 f f f c c a a f f a a . . 
        . 8 8 8 8 a a 3 3 3 3 1 3 a a . 
        8 8 8 8 8 8 a a 3 3 3 1 3 3 a a 
        8 8 8 8 8 8 a a 3 3 3 3 1 3 a a 
        `,img`
        . . . . . . . c d . . . . . . . 
        . . . . . . . c d . . . . . . . 
        . . . . . . . c d . . . . . . . 
        . . . . . . . c b . . . . . . . 
        . . . . . . . f f . . . . . . . 
        . . . . . . . c 6 . . . . . . . 
        . . . . . . . f f . . . . . . . 
        . . . . . . . 8 6 . . . . . . . 
        . . . . . . 8 8 9 8 . . . . . . 
        . . . . . . 8 6 9 8 . . . . . . 
        . . . . . c c c 8 8 8 . . . . . 
        . . . . 8 8 6 6 6 9 8 8 . . . . 
        . . 8 f f f c c e e f f 8 8 . . 
        . 8 8 8 8 8 8 6 6 6 6 9 6 8 8 . 
        8 8 8 8 8 8 8 8 6 6 6 9 6 6 8 8 
        8 8 8 8 8 8 8 8 6 6 6 6 9 6 8 8 
        `],
    500,
    true
    )
}
info.onLifeZero(function () {
    game.over(false, effects.splatter)
})
sprites.onDestroyed(SpriteKind.Player, function (sprite) {
    if (info.life() > 0) {
        pause(2000)
        Create_Player()
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.fire, 500)
    music.smallCrash.play()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 500)
    music.smallCrash.play()
    info.changeLifeBy(-1)
})
let baddie: Sprite = null
let player_rocket: Sprite = null
let bullet: Sprite = null
let maximum_bullets_on_screen = 0
info.setLife(3)
maximum_bullets_on_screen = 3
let number_of_baddies = 5
effects.starField.startScreenEffect()
Create_Player()
forever(function () {
    if (sprites.allOfKind(SpriteKind.Enemy).length < number_of_baddies) {
        baddie = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . 8 8 . . . . . . . 
            . . . . . . 8 8 8 8 . . . . . . 
            . . . . . 8 8 8 8 8 8 . . . . . 
            . . . . 8 8 8 8 8 8 8 8 . . . . 
            . . . . 8 8 8 8 8 8 8 8 . . . . 
            . . . 8 8 8 2 8 8 2 8 8 8 . . . 
            . . . 8 8 8 8 8 8 8 8 8 8 . . . 
            . . . 8 8 8 8 8 8 8 8 8 8 . . . 
            . . . 8 8 8 8 8 8 8 8 8 8 . . . 
            . . . 8 8 8 8 2 2 8 8 8 8 . . . 
            . . . 8 8 8 2 8 8 2 8 8 8 . . . 
            . . . 8 8 8 8 8 8 8 8 8 8 . . . 
            . . . 8 . . 8 . . 8 . 8 . . . . 
            . . . . 8 . 8 . 8 . . . 8 . . . 
            . . . 8 . . 8 . . 8 . 8 . . . . 
            `, SpriteKind.Enemy)
    }
    pause(randint(1000, 5000))
})
