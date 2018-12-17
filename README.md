# Threads

## Pros/Cons
- So easy to do
- There's memory overhead to each thread
- CPU overhead in thread management
- Global / shared data is not reliable

# Callbacks

## Pros/Cons
- (language dependent) Can maintain more streams of execution with lower overhead
- Execution chain is broken, which can make debugging harder

# Coroutines

## Pros/Cons
- Overhead, state safety advantages of Callbacks
- Sequential reasoning, predictable debugging advantages of Threads
- Generator equiv might not exist in your language
