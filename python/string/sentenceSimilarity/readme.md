# 1813. Sentence Similarity 3

You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

### Examples

---

Example 1:

Input: s1 = "Hello Jane" , s2 = "Hello my name is Jane"
Output: true
Explanation : Can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.

Example 2:

Input: s1 = "Frog cool", s2 = "Frogs are cool"
Output: false
Explanation : Are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.

Constraints:
1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.

Solution code - insertSentence.py
Solution Overview - Using 2 pointers check for prefix and suffix.
