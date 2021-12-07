import System.IO
import System.Environment
import Data.List

-- | Write code in lambda function
-- | and run the code using `aoc` command
main :: IO ()
main = interact (\s -> applyLines sort s)

applyLines :: (String -> String) -> String -> String
applyLines f = unlines . map f . lines
