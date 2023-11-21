import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") # 練習１：背景画像Surfaceの生成
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]
    kk_img = pg.image.load("ex01/fig/3.png") # 練習２：こうかとん画像Surfaceの生成
    kk_img = pg.transform.flip(kk_img, True, False) # 練習２：こうかとんの左右反転
    kk_imgs = [pg.transform.rotozoom(kk_img, i, 1.0)for i in range(11)] # 練習３：こうかとんSurfaceのリスト
    count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_imgs[0], [-x, 0]) # 練習４：背景画像の表示
        screen.blit(bg_imgs[1], [1600-x, 0]) # 練習６：動く背景画像
        screen.blit(bg_imgs[0], [3200-x, 0])
        screen.blit(kk_imgs[count[tmr%20]], [300, 200]) # 練習５：こうかとんはばたく
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()