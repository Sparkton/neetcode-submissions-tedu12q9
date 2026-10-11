struct MyHashSet {
    data: Vec<bool>,
}

impl MyHashSet {
    pub fn new() -> Self {
        Self {
            data: vec![false; 1_000_001]
        }
    }

    pub fn add(&mut self, key: i32) {
        self.data[key as usize] = true;
    }

    pub fn remove(&mut self, key: i32) {
        self.data[key as usize] = false;
    }

    pub fn contains(&self, key: i32) -> bool {
        self.data[key as usize]
    }
}
