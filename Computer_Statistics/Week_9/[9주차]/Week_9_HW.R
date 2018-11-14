Alice <<- NULL
Bob <<- NULL

game <- function(){
  break_num = 0
  alice = 0
  bob = 0
  repeat{
    break_num = break_num + 1
    if(break_num == 100){
      break
    }
    num = sample(1:10,1)
    if(num %% 2 == 1){
      alice = alice + 1
    }
    else{
      bob = bob + 1
    }
  }
  Alice <<- append(Alice, alice)
  print("Alice ==> ")
  print(Alice)
  print("")
  Bob <<- append(Bob, bob)
  print("Bob ==>")
  print(Bob)
  print("------------------------------")
}
game()
game()
game()
game()
game()
game()
game()
game()
game()
game()

mean(Alice)
