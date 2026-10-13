impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let new_str: Vec<char> = s
            .chars()
            .filter(|b| b.is_ascii_alphanumeric())
            .map(|b| b.to_ascii_lowercase())
            .collect();
        // new_str == new_str.iter().copied().rev().collect::<Vec<u8>>()
        new_str.iter().eq(new_str.iter().rev())
        // println!("{:?}", &new_str);

        // true
    }
}
