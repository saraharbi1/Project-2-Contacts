from person import Person

class Contacts(list):
    

    def count_duplicates(self) -> int:
       
        seen = []       
        duplicates = [] 

        for person in self:

            already_seen = any(person == s for s in seen)
            if not already_seen:
                seen.append(person)
            else:
                if not any(person == d for d in duplicates):
                    duplicates.append(person)
        return len(duplicates)
