 for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image1, each.rect)
                else:
                    if not(delay % 3):
                        if e1_destroy_index ==0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index+1)%4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()   
 
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
