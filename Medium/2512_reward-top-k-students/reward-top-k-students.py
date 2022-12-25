class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos, neg, transcript = set(positive_feedback), set(negative_feedback), []
        for id, comment in zip(student_id, report):
            points = 0
            for word in comment.split():
                if word in pos:
                    points += 3
                elif word in neg:
                    points -= 1
            transcript.append((-points, id))
        return [id for _, id in sorted(transcript)[:k]]
