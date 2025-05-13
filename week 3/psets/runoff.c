#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Max number of voters and candidates allowed
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] stores j-th ranked candidate index for i-th voter
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidate structure holds their name, vote count, and eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array to store all candidates
candidate candidates[MAX_CANDIDATES];

// Number of voters and candidates (will be set in main)
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check if at least one candidate is passed in command line
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Set total number of candidates
    candidate_count = argc - 1;

    // Exit if candidate count exceeds maximum allowed
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }

    // Initialize each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];  // Candidate name from command-line argument
        candidates[i].votes = 0;           // Votes start at 0
        candidates[i].eliminated = false;  // No one eliminated at start
    }

    // Prompt user for number of voters
    voter_count = get_int("Number of voters: ");

    // Check if voter count exceeds maximum
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Loop over every voter
    for (int i = 0; i < voter_count; i++)
    {
        // Prompt for each voter's ranked preferences
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Try to record the vote, exit on invalid input
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");  // Blank line between voters
    }

    // Run runoff process repeatedly until someone wins
    while (true)
    {
        // Count votes for non-eliminated candidates
        tabulate();

        // Check if someone won (has majority)
        bool won = print_winner();
        if (won)
        {
            break;  // Exit loop if there's a winner
        }

        // No winner, so find minimum vote count among remaining candidates
        int min = find_min();

        // Check if election is tied (all remaining candidates have same votes)
        bool tie = is_tie(min);

        // If tied, print all remaining candidates as winners
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;  // End the election on tie
        }

        // Eliminate all candidates who have the minimum vote count
        eliminate(min);

        // Reset all vote counts to 0 before next round
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }

    return 0;
}

// Register a vote if name matches a candidate
bool vote(int voter, int rank, string name)
{
    for (int k = 0; k < candidate_count; k++)
    {
        // Compare entered name with candidate name
        if (strcmp(candidates[k].name, name) == 0)
        {
            preferences[voter][rank] = k;  // Store candidate index in preferences
            return true;
        }
    }
    return false;  // No candidate matched
}

// Count top-ranked non-eliminated candidates for each voter
void tabulate(void)
{
    for(int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            int index = preferences[i][j];  // Get j-th preference for i-th voter

            // If candidate has not been eliminated, count the vote
            if (!candidates[index].eliminated)
            {
                candidates[index].votes++;  // Add one vote
                break;  // Stop after first valid candidate (highest non-eliminated preference)
            }
        }
    }

    return;
}

// Print name of candidate who has more than half of total votes
bool print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // Majority check: > 50% of total voters
        if (candidates[i].votes > voter_count / 2)
        {
            printf("%s\n", candidates[i].name);  // Print winner's name
            return true;
        }
    }
    return false;  // No winner yet
}

// Find the minimum vote count among all non-eliminated candidates
int find_min(void)
{
    int min = INT_MAX;

    for (int i = 0; i < candidate_count; i++)
    {
        // Consider only non-eliminated candidates
        if (!candidates[i].eliminated && candidates[i].votes < min)
        {
            min = candidates[i].votes;
        }
    }

    return min;
}

// Check if all remaining candidates are tied (have same vote count)
bool is_tie(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // If any remaining candidate has more than min votes, it's not a tie
        if (!candidates[i].eliminated && candidates[i].votes > min)
        {
            return false;
        }
    }
    return true;  // All remaining candidates are tied
}

// Eliminate all candidates who have vote count equal to min
void eliminate(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // Only eliminate if not already eliminated and vote count is equal to min
        if (!candidates[i].eliminated && candidates[i].votes == min)
        {
            candidates[i].eliminated = true;  // Mark candidate as eliminated
        }
    }
    return;
}
