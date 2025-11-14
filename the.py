  if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT: screen.blit(judge_left.image, (100, 0))
            
         elif event.key == pygame.K_DOWN: sys.exit()
         elif event.key == pygame.K_UP: sys.exit()
         elif event.key == pygame.K_RIGHT: sys.exit()