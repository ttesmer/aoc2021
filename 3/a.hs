import System.IO
import System.Environment
import Data.List
import Data.Char
import Control.Arrow
import Data.Function

main :: IO ()
main = interact (\s -> (show $ (gamma s)*(epsilon s)) ++ "\n")
    where gamma = f maximumBy
          epsilon = f minimumBy

f :: Ord a1 =>
     (((a2, a1) -> (a2, a1) -> Ordering) -> [(Char, Int)] -> (Char, b))
     -> String -> Int
f fun s = toDec $ (\xs 
        -> fst . fun (compare `on` snd) 
             $ map (head &&& length) . group . sort $ xs) 
       <$> (transpose . lines $ s)

toDec :: String -> Int
toDec = foldl' (\acc x -> acc * 2 + digitToInt x) 0
