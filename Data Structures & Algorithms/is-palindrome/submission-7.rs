impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let new_str: Vec<u8> = s
            .bytes()
            .filter(|b| b.is_ascii_alphanumeric())
            .map(|b| b.to_ascii_lowercase())
            .collect();
        new_str == new_str.iter().copied().rev().collect::<Vec<u8>>()
    }
}
