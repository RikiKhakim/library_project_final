from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # correctness of the input values
        if not title.isalpha() & author.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Noto'g'ri kiritildi title yoki author!"
                }
            )

        # checking the existence in database
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Bunday kitob mavjud"
                }
            )

        return data
