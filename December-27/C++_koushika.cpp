bool must_be_2x2(std::vector<std::vector<std::string>>& letters)
{
    constexpr int MIN_SIZE = 2;
    if (letters.at(0).size() > MIN_SIZE && letters.at(1).size() > MIN_SIZE)
    {
        return true;
    }

    return false;
}

std::string matrix_vector_to_string(std::vector<std::vector<std::string>>& matrix)
{
    std::string str;

    for (int row = 0; row < matrix.size(); ++row)
    {
        for (int col = 0; col < matrix.at(row).size(); ++col)
        {
            str += matrix.at(row).at(col);
        }
    }

    return str;
}

bool alphabet_only(std::vector<std::vector<std::string>>& letters)
{
    std::string str = matrix_vector_to_string(letters);

    for (std::size_t pos = 0; pos < str.length(); ++pos)
    {
        if (!std::isalpha(str.at(pos)))
        {
            return false;
        }
    }

    return true;
}

bool equal_length(std::vector<std::vector<std::string>>& letters)
{
    const size_t SIZE = letters.at(0).size();

    for (std::size_t row = 1; row < letters.size(); ++row)
    {
        if (letters.at(row).size() != SIZE)
        {
            return false;
        }
    }

    return true;
}

bool is_vowel(std::string element) noexcept
{
    static const auto vowels = std::array<std::string,5> { "a","e","i","o","u" };

    return std::find(vowels.begin(), vowels.end(), element) != vowels.end();
}

std::string find_vowel_square(std::vector<std::vector<std::string>>& letters)
{
    for (std::size_t row = 0; row < letters.size()-1; ++row)
    {
        for (std::size_t col = 0; col < letters.at(row).size()-1; ++col)
        {
            if (is_vowel(letters.at(row).at(col)) && is_vowel(letters.at(row).at(col + 1)) && is_vowel(letters.at(row + 1).at(col)) && is_vowel(letters.at(row).at(col + 1)))
            {
                return std::to_string(row) + "-" + std::to_string(col);
            }
        }
    }
