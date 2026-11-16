ENV_FILE="$PROJECT_DIR/.env"

case "$ENVIRONMENT" in
    development)
        COMPOSE_OVERRIDE="$PROJECT_DIR/compose.override.yaml"
        ;;
    production)
        COMPOSE_OVERRIDE="$PROJECT_DIR/compose.prod.yaml"
        ;;
    *)
        echo "Unknown environment: $ENVIRONMENT" >&2
        exit 2
        ;;
esac

if [ ! -f "$ENV_FILE" ]; then
    echo "Environment file not found: $ENV_FILE" >&2
    exit 1
fi
