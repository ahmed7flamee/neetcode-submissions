class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diccionario = {}
        for palabra in strs:
            firma = "".join(sorted(palabra))
            if firma in diccionario:
                diccionario[firma].append(palabra)

            else:
                diccionario[firma] = [palabra]

        return list(diccionario.values())

        