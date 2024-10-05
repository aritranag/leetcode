/**
 * Checks for whether a string is vowel or not
 * @param {string} char A single character string which is identified to be vowel or not
 * @return {number} 1/0 returns 1 for vowel, 0 for consonant
 */
function isVowel(char) {
    let vowel_list = "aeiou";
    if (vowel_list.indexOf(char) > -1) {
        return 1;
    } else {
        return 0;
    }
}

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function (s, k) {
    // create a new window of the same length to hold 1/0 for each character based on whether they are vowel or not
    let window = new Array(s.length);
    let string_length = s.length;

    // each character needs to be checked for vowel, this check is being done beforehand
    for (i = 0; i < string_length; i++) {
        window[i] = isVowel(s.charAt(i));
    }

    // create the sliding window for the first k characters
    let sliding_window = window.slice(0, k);

    // count of the vowels in the window, this will be updated for every window
    let running_count = sliding_window.reduce((acc, curVal) => acc + curVal, 0);

    // count variable for storing the max count
    let max_count = running_count > 0 ? running_count : 0;

    // iterate through the entire modified array of 1/0 for counts
    // each step it removes the count for the left side of the window and adds the value of the right side
    // max count if needed is updated
    for (i = 0; i < string_length - k; i++) {
        running_count -= window[i];
        running_count += window[i + k];
        max_count = max_count > running_count ? max_count : running_count;
    }

    return max_count;
};

s = "abciiidef";
k = 5;
console.log(maxVowels(s, k));
