"""
James Jang
9/27/2024
This program decodes text typed in through a malfunctioning keyboard
"""


def main():
	
	#encoded_word = "WBLARF8TTS"
	#encoded_word = "L8KAOUL"
	#encoded_word = "E8N8N8"
	#encoded_word = "8TRA8DY T8LA"
	#encoded_word = "8TT LHA TILLTA LIMAS"	
	#encoded_word = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encoded_word = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	encoded_word = "UUHO"  		#Used for Bonus
	encoded_word = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encoded_word))






def DecodeWord(encoded_word):
	decoded_word = ""
	decoded_word = encoded_word
	index = 0
	while index <= len(decoded_word) - 1:
		if decoded_word[index] == 'T':
			decoded_word = decoded_word[:index]+'L'+decoded_word[index+1:]
			index += 1
			continue
		if decoded_word[index] == 'L':
			decoded_word = decoded_word[:index]+'T'+decoded_word[index+1:]
			index += 1
			continue
		if decoded_word[index] == 'B' or decoded_word[index] == '8':
			decoded_word = decoded_word[:index]+'A'+decoded_word[index+1:]
			index += 1
			continue
		if decoded_word[index] == 'A':
			decoded_word = decoded_word[:index]+'E'+decoded_word[index+1:]
			index += 1
			continue
		if decoded_word[index] == 'E':
			decoded_word = decoded_word[:index]+'B'+decoded_word[index+1:]
			index += 1
			continue	
		if index <= len(decoded_word)-2 and decoded_word[index]+decoded_word[index+1] == 'UU':
			decoded_word = decoded_word[:index]+'W'+decoded_word[index+2:]
			index += 1
			continue		
		else:
			index += 1
			
	return decoded_word



#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
