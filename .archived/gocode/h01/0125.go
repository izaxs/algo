package h01

func isPalindrome(s string) bool {
	lo, hi := 0, len(s)-1
	for lo < hi {
		if !isAlnum(s[lo]) {
			lo++
		} else if !isAlnum(s[hi]) {
			hi--
		} else if toLower(s[lo]) == toLower(s[hi]) {
			lo++
			hi--
		} else {
			return false
		}
	}
	return true
}

func isAlnum(b byte) bool {
	return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
	// return unicode.IsLetter(r) || unicode.IsDigit(r)
}

func toLower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + 32
	}
	return b
}
